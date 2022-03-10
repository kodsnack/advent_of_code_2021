import 'package:flutter/material.dart';

class Day16 extends StatelessWidget {
  Day16({Key? key}) : super(key: key);
  static String routeName = 'day16';
  final bool isExample = false;
  static String dayTitle = 'Day 16: Packet Decoder';

  @override
  Widget build(BuildContext context) {
    final resultPart1 = doPart1();
    final resultPart2 = doPart2();
    return Scaffold(
      appBar: AppBar(
        title: Text(dayTitle),
      ),
      body: Center(
        child: Column(
          children: [
            const SizedBox(
              height: 200,
            ),
            SelectableText('Svar dag 16 del 1: $resultPart1'),
            SelectableText('Svar dag 16 del 2 : $resultPart2'),
          ],
        ),
      ),
    );
  }

  late BinaryProvider baseBinaryProvider;

  int doPart1() {
    String hexStr = getInput(isExample);
    String binaryStr = convertToBinary(hexStr);
    baseBinaryProvider = BinaryProvider(binaryStr);
    int result = decodeStrPart1(baseBinaryProvider);

    return result;
  }

  int doPart2() {
    String hexStr = getInput(isExample);
    String binaryStr = convertToBinary(hexStr);
    baseBinaryProvider = BinaryProvider(binaryStr);
    int result = decodeStrPart2(baseBinaryProvider);

    return result;
  }

  String getInput(bool example) {
    if (example) {
      return exampleInputText;
    } else {
      return inputText;
    }
  }

  String convertToBinary(String hexStr) {
    String s = '';
    for (int i = 0; i < hexStr.length; i++) {
      int code = int.parse(hexStr[i], radix: 16);
      String binary = code.toRadixString(2);
      while (binary.length < 4) {
        binary = '0' + binary;
      }
      s += binary;
    }
    return s;
  }

  int decodeStrPart1(BinaryProvider binaryProvider) {
    Packet? packet = getPacket(binaryProvider);

    return packet.countVersionSum();
  }

  int decodeStrPart2(BinaryProvider binaryProvider) {
    Packet basePacket = getPacket(binaryProvider);
    int value = basePacket.evaluate();
    return value;
  }

  int getLiteral(BinaryProvider binaryProvider) {
    int value = 0;
    String continueBit = binaryProvider.getBits(1);
    while (continueBit == '1') {
      value = value * 16 + int.parse(binaryProvider.getBits(4), radix: 2);
      continueBit = binaryProvider.getBits(1);
    }
    value = value * 16 + int.parse(binaryProvider.getBits(4), radix: 2);
    return value;
  }

  Packet getOperatorPacket(BinaryProvider binaryProvider, int version, int packetType) {
    int lengthTypeId = int.parse(binaryProvider.getBits(1), radix: 2);
    late Packet opPacket;
    if (lengthTypeId == 0 ) {
      int bitLength = int.parse(binaryProvider.getBits(15), radix: 2);
      opPacket = OperatorPacket(version, packetType, bitLength: bitLength, operatorSubPacketType: operatorSubPacketTypes.withBitLength);
      BinaryProvider subBinaryProvider = BinaryProvider(binaryProvider.getBits(bitLength));
      List<Packet>? subPackets = getSubPacketsWithBitLength(subBinaryProvider);
      opPacket.subPackets = [...opPacket.subPackets, ...subPackets];
    }
    if ( lengthTypeId == 1) {
      int noOfSubPackets = int.parse(binaryProvider.getBits(11), radix: 2);
      opPacket = OperatorPacket(version, packetType, noOfSubPackets: noOfSubPackets, operatorSubPacketType: operatorSubPacketTypes.withNoOfSubPackets);
      for ( int packetNo = 0 ; packetNo < noOfSubPackets; packetNo++) {
        opPacket.subPackets.add(getPacket(binaryProvider));
      }
    }
    return opPacket;
  }

  int getValue(BinaryProvider binaryProvider, int len) {
    String s = binaryProvider.getBits(len);
    int value = int.parse(s, radix: 2);
    return value;
  }

  Packet getPacket(BinaryProvider binaryProvider) {
    int version = getValue(binaryProvider, 3);
    int packetType = getValue(binaryProvider, 3);
    if (packetType == 4) {
      // Literal
      final literal = getLiteral(binaryProvider);
      final packet = LiteralPacket(version, packetType, literal);
      return packet;
    } else {
      // Operator packet
      final operatorPacket = getOperatorPacket(binaryProvider, version, packetType);
      return operatorPacket;
    }
  }

  List<Packet> getSubPacketsWithBitLength(BinaryProvider binaryProvider) {
    List<Packet> subPacketList = [];
    while (binaryProvider.hasBits()) {
      Packet packet = getPacket(binaryProvider);
      subPacketList.add(packet);
    }
    return subPacketList;
  }
}


class BinaryProvider {
  String binaryStr;

  BinaryProvider(this.binaryStr);

  String getBits(int length) {
    String s = binaryStr.substring(0, length);
    binaryStr = binaryStr.substring(length);
    return s;
  }

  bool hasBits() {
    return binaryStr.isNotEmpty;
  }
}

enum operationTypes { sum, product, minimum, maximum, literal, greaterThan, lessThan, equal}

abstract class Packet {
  int version;
  int packetType;

  List<Packet> subPackets =[];

  Packet(this.version, this.packetType);

  int countVersionSum() {
    int sum = 0;
    for ( final packet in subPackets) {
      sum += packet.countVersionSum();
    }
    return sum + version;
  }

  int evaluate();

}

class LiteralPacket extends Packet{
  int value;

  LiteralPacket(int version, int packetType, this.value) : super(version, packetType);

  @override
  int evaluate() {
    return value;
  }

}

enum operatorSubPacketTypes { withBitLength, withNoOfSubPackets}

class OperatorPacket extends Packet {
  int? bitLength;
  int? noOfSubPackets;
  operatorSubPacketTypes operatorSubPacketType;

  OperatorPacket(int version, int packetType, {this.bitLength, this.noOfSubPackets, required this.operatorSubPacketType}) : super(version, packetType);

  @override
  int evaluate() {
    switch ( operationTypes.values[packetType] ) {
      case operationTypes.sum: {
        return sumSubPackets();
      }
      case operationTypes.product: {
        return multiplySubPackets();
      }
      case operationTypes.minimum: {
        return minOfSubPackets();
      }
      case operationTypes.maximum: {
        return maxOfSubPackets();
      }
      case operationTypes.greaterThan: {
        return firstSubPacketGreaterThanSecond();
      }
      case operationTypes.lessThan: {
        return firstSubPacketLessThanSecond();
      }
      case operationTypes.equal: {
        return firstSubPacketEqualToSecond();
      }
      default:
        return 0;
    }
  }

  int sumSubPackets() {
    int sum = 0 ;
    for ( final packet in subPackets) {
      sum += packet.evaluate();
    }
    return sum;
  }

  int multiplySubPackets() {
    int product = 1 ;
    for ( final packet in subPackets) {
      product *= packet.evaluate();
    }
    return product;
  }

  int minOfSubPackets() {
    bool start = true;
    late int min;
    for ( final packet in subPackets) {
      if ( start ) {
        start = false;
        min = packet.evaluate();
      } else {
        int subValue = packet.evaluate();
        if (subValue < min ) min = subValue;
      }
    }
    return min;
  }

  int maxOfSubPackets() {
    bool start = true;
    late int max;
    for ( final packet in subPackets) {
      if ( start ) {
        start = false;
        max = packet.evaluate();
      } else {
        int subValue = packet.evaluate();
        if (subValue > max ) max = subValue;
      }
    }
    return max;
  }

  int firstSubPacketGreaterThanSecond() {
    if ( subPackets[0].evaluate() > subPackets[1].evaluate()) return 1;
    return 0;
  }

  int firstSubPacketLessThanSecond() {
    if ( subPackets[0].evaluate() < subPackets[1].evaluate()) return 1;
    return 0;
  }

  int firstSubPacketEqualToSecond() {
    if ( subPackets[0].evaluate() == subPackets[1].evaluate()) return 1;
    return 0;
  }

}
class ValueAndLength {
  int value;
  int length;

  ValueAndLength(this.value, this.length);
}


String exampleInputText = '''9C0141080250320F1802104A08''';

String inputText =
    '''E20D72805F354AE298E2FCC5339218F90FE5F3A388BA60095005C3352CF7FBF27CD4B3DFEFC95354723006C401C8FD1A23280021D1763CC791006E25C198A6C01254BAECDED7A5A99CCD30C01499CFB948F857002BB9FCD68B3296AF23DD6BE4C600A4D3ED006AA200C4128E10FC0010C8A90462442A5006A7EB2429F8C502675D13700BE37CF623EB3449CAE732249279EFDED801E898A47BE8D23FBAC0805527F99849C57A5270C064C3ECF577F4940016A269007D3299D34E004DF298EC71ACE8DA7B77371003A76531F20020E5C4CC01192B3FE80293B7CD23ED55AA76F9A47DAAB6900503367D240522313ACB26B8801B64CDB1FB683A6E50E0049BE4F6588804459984E98F28D80253798DFDAF4FE712D679816401594EAA580232B19F20D92E7F3740D1003880C1B002DA1400B6028BD400F0023A9C00F50035C00C5002CC0096015B0C00B30025400D000C398025E2006BD800FC9197767C4026D78022000874298850C4401884F0E21EC9D256592007A2C013967C967B8C32BCBD558C013E005F27F53EB1CE25447700967EBB2D95BFAE8135A229AE4FFBB7F6BC6009D006A2200FC3387D128001088E91121F4DED58C025952E92549C3792730013ACC0198D709E349002171060DC613006E14C7789E4006C4139B7194609DE63FEEB78004DF299AD086777ECF2F311200FB7802919FACB38BAFCFD659C5D6E5766C40244E8024200EC618E11780010B83B09E1BCFC488C017E0036A184D0A4BB5CDD0127351F56F12530046C01784B3FF9C6DFB964EE793F5A703360055A4F71F12C70000EC67E74ED65DE44AA7338FC275649D7D40041E4DDA794C80265D00525D2E5D3E6F3F26300426B89D40094CCB448C8F0C017C00CC0401E82D1023E0803719E2342D9FB4E5A01300665C6A5502457C8037A93C63F6B4C8B40129DF7AC353EF2401CC6003932919B1CEE3F1089AB763D4B986E1008A7354936413916B9B080''';
