import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

import 'models/segment_input.dart';

class Day8 extends StatelessWidget {
  const Day8({Key? key}) : super(key: key);
  static String routeName = 'day8';
  final bool isExample = false;
  static String dayTitle = 'Day 8: Seven Segment Search';

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
            SelectableText('Svar dag 8 del 1: $resultPart1'),
            SelectableText('Svar dag 8 del 2 : $resultPart2'),
          ],
        ),
      ),
    );
  }

  int doPart1() {
    final inputs = getInput(isExample);
    List<int> wantedNoOfSegments = [2,4,3,7];
    int count = 0;
    for (final input in inputs ) {
      for ( final segment in input.actualInputSegments) {
        if (wantedNoOfSegments.contains(segment.length)) {
          count++;
        }
      }
    }
    return count;
  }

  int doPart2() {
    final inputs = getInput(isExample);
    // Loop through each input line
    int result = 0;
    for ( final input in inputs) {
      final conversionMap = calcSegments(input);
      final digits = getDigitsFromInput(conversionMap, input);
      result += int.parse(digits);
    }
    return result;
  }

  String getDigitsFromInput(Map<segmentNames, segmentNames> conversionMap, SegmentInput input) {
    String digits = '';
    for (final segments in input.actualInputSegments) {
      Set<segmentNames> realSegments = {};
      for ( String segment in segments.split('')) {
        segmentNames seg = conversionMap[segmentNames.values.byName(segment)]!;
        realSegments.add(seg);
      }
      digits += getDigitFromSegments(realSegments);
    }
    return digits;
  }


  String getDigitFromSegments( Set<segmentNames> segments) {
    for ( int i = 0 ; i < digitList.length; i++) {
      if (setEquals(segments, digitList[i])) {
        return i.toString();
      }
    }
    return '';
  }

  Map<segmentNames,segmentNames> calcSegments(SegmentInput input) {
    // Make a list for each digit that contains a set of segments for it
    List<Set<segmentNames>> segmentsForDigit = List.filled(10, {});
    List<Set<segmentNames>> digitsWith5Segments = [];
    List<Set<segmentNames>> digitsWith6Segments = [];

    // Loop through all example segments
    for ( int i = 0 ; i < input.exampleSegments.length; i++) {
      // Put the segments into a set
      Set<segmentNames> segSet = {};
      for (final nameStr in input.exampleSegments[i].split('')) {
        segSet.add(segmentNames.values.byName(nameStr));
      }

      // Check for the unique length for digits 1 (2 segments lit), 4 (4 segs), 7 (3) and 8 (7)
      // If the number of segments lit is 5, the digit is either a 2, 3 or a 5. Make a list of these
      // If the number of segments lit is 6, the digit is either a 0, 6 or a 9. Make a list of these 2 also
      switch (segSet.length) {
        case 2 : // Must be digit 1
          segmentsForDigit[1] = segSet;
          break;
        case 3 : // Must be digit 7
          segmentsForDigit[7] = segSet;
          break;
        case 4 : // Must be digit 4
          segmentsForDigit[4] = segSet;
          break;
        case 5 : // Must be digit 2, 3 or 5
          digitsWith5Segments.add( segSet );
          break;
        case 6 : // Must be digit 6 or 9
          digitsWith6Segments.add( segSet );
          break;
        case 7 : // Must be digit 8
          segmentsForDigit[8] = segSet;
          break;
        default :
          throw ( Exception('Something went wrong in segment analysis'));
      }
    }

    // Digits 1, 4, 7 and 8 are found.
    // The top horizontal segment (a) is in digit 7 but not in digit 1. Find it
    segmentNames aSegment = segmentsForDigit[7].difference(segmentsForDigit[1]).single;

    // Digit 3 has 5 segments and also contains the same segments as digits 7 and 1.
    // Therefore we can calculate the other two horizontal segments
    Set<segmentNames> segmentsDandG = {};
    for ( final segSet in digitsWith5Segments) {
      if ( segSet.containsAll(segmentsForDigit[7])) {
        segmentsDandG = segSet.difference(segmentsForDigit[7]);
      }
    }

    if (segmentsDandG.length != 2 ) {
      throw (Exception('Should be 2 segments here!'));
    }

    // Digit 4 has horizontal segment d lit so now we can determine both seg d and G from the previous solution
    segmentNames dSegment = segmentsDandG.intersection(segmentsForDigit[4]).single;
    // and segment g is the other one
    segmentNames gSegment = segmentsDandG.difference({dSegment}).single;

    // All horizontal segments are found.
    // Digit 4 has segment b lit so we can get this segment by removing c and f ( from digit 1 ) and segment d;
    Set<segmentNames> segmentsCandF = {segmentsForDigit[1].first, segmentsForDigit[1].last};
    segmentNames bSegment = segmentsForDigit[4].difference(segmentsCandF).difference({dSegment}).single;

    // These segments ready now
    //     aaaaaa
    //    b      .
    //    b      .
    //    b      .
    //     dddddd
    //    .      .
    //    .      .
    //    .      .
    //     gggggg
    // Segments c, e and f left.
    // e segment should be the remaining one if we remove the known segments and segments c and f
    // from all segments. All segments are found in digit 8
    segmentNames eSegment = segmentsForDigit[8].difference(segmentsCandF).difference({aSegment, bSegment, dSegment,gSegment}).single;

    // Segment b, d and e are lit in digit 6. This is unique among the 6 segments digits
    // so we now can find the remaining two segments

    late segmentNames fSegment , cSegment;
    for ( final segSet in digitsWith6Segments) {
      if ( segSet.containsAll({bSegment, dSegment, eSegment}) ) {
        cSegment = segmentsCandF.difference(segSet).single;
        fSegment = segmentsCandF.intersection(segSet).single;
      }
    }

    // All segments are found. Now make a map from the wrong segments to the correct one.
    Map<segmentNames, segmentNames> correctionMap = {
      aSegment :  segmentNames.a,
      bSegment : segmentNames.b,
      cSegment  : segmentNames.c ,
      dSegment : segmentNames.d ,
      eSegment : segmentNames.e ,
      fSegment : segmentNames.f,
      gSegment : segmentNames.g,
    };
    return correctionMap;
  }


}

enum segmentNames {a,b,c,d,e,f,g}

List<Set<segmentNames>> digitList = [
  {segmentNames.a, segmentNames.b,segmentNames.c,segmentNames.e,segmentNames.f,segmentNames.g}, // Digit 0
  {segmentNames.c, segmentNames.f}, // digit 1
  {segmentNames.a, segmentNames.c, segmentNames.d, segmentNames.e,segmentNames.g}, // 2
  {segmentNames.a, segmentNames.c, segmentNames.d, segmentNames.f, segmentNames.g }, // 3
  {segmentNames.b, segmentNames.c, segmentNames.d, segmentNames.f}, // 4
  {segmentNames.a, segmentNames.b, segmentNames.d, segmentNames.f, segmentNames.g}, // 5
  {segmentNames.a, segmentNames.b, segmentNames.d, segmentNames.e, segmentNames.f, segmentNames.g}, // 6
  {segmentNames.a, segmentNames.c, segmentNames.f}, // 7
  {segmentNames.a, segmentNames.b, segmentNames.c, segmentNames.d, segmentNames.e, segmentNames.f, segmentNames.g}, // 8
  {segmentNames.a, segmentNames.b, segmentNames.c, segmentNames.d, segmentNames.f, segmentNames.g}, // 9
];

List<SegmentInput> getInput(bool example) {
  late String text;
  if (example) {
    text = exampleInputText;
  } else {
    text = inputText;
  }
  List<String> lines = text.split('\n');
  List<SegmentInput> segments = [];
  for ( String line in lines ) {
    List<String> inputs = line.split(' | ');
    List<String> exampleSegments = inputs[0].split(' ');
    List<String> actualSegmentInput = inputs[1].split(' ');
    SegmentInput segmentInput = SegmentInput(exampleSegments, actualSegmentInput);
    segments.add(segmentInput);
  }
  return segments;
}

String exampleInputText =
'''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce''';

String inputText =
'''aedcg db ecbdgf badfegc abfcde edb cbgfe bfdg bdgec agfbce | ecagd gcbde dbcefa bgfd
bgeadf egcbda cfebg ac caefbdg bacd ecfgad cabeg gca abgde | gcbef befcg ac ac
cbfge ed aegbcd gfdba aedf facbdge fdegba bfgcda befdg dge | adbgef dfgbe dbgfe agdfb
efdga dgebfc cefa edgfc decbagf cdagfe ade bgafd ae cadbge | adfcegb dgcfabe ea cbfdge
fe bdcge ecfbdg ecf bdfe gdacbe gdefcab gfcad cdgef ceagbf | ef bdceg begdafc efgdc
gfacedb bfgadc fbdgec eagcb cdfe cd gcd afedbg bdceg gfdeb | dcg gecdb adebfg cdbeg
bfecadg fdbage bdgfca cfba fdceg acdgeb dfa af acgbd gadcf | fad bacf adbgce gbdafc
fbaeg dbcegf acgfbd gadbecf bfagce ge bedfa bfagc cage efg | adbef gfcdeb bdgcaf dbegfc
bcad gcefbad afbdg cgfea gfedba dcbegf dagbfc gfcab cb gcb | bc cbfadeg ecfdgb gbc
eabgcd eagfbd fdgb gbdea dbaecgf fbe bf fdcbea gfeba faegc | egafc fbdg dabgefc agdeb
cf fabdg fbeagc gefc bfc caegb gbeacd cgafb cadbfe fagdecb | eabdcf bdeafcg acgbe fceg
acdgb gbcfe fbdecga df cgafed efbagc bcgdf dfgcbe fgd fbed | dbcag cfdgb dgfcbe gaecfb
fc cebad fdagb fbc gbfade dcfgbe dfcba gcaf degcfab afgcdb | gefbda bgcfde bfc gadfeb
cfagdb gfbd fg badgfce gfc ecdbfa bdfac gdafc fgeacb edacg | bfdca bgfd bgacfd gf
fae ebgad cgfba bdfagc fe ebfgdca bacdfe cabegf egbaf egfc | ef efdcba abdfce agcbf
gebfd aecf ecgab cbagfd cf gfecba dcbgafe cebfg dcbgea cbf | ebcagf fc acdfbg cfdbag
agfed fdaegcb facb ba bedfc abe edfba begadc gcdefb dfcaeb | becfd bea acbf ebdgcf
dfb fbdae eagcbf baegd fbcea cfde aedcfb df gabdfc fgadceb | adfbe badef gdbcaf ecfd
acdbg ebaf fcadge bgf dfgae gdafb fb gcfebda fegdba gcfdbe | agfced degafc bf cbdga
ecadg gf dgabfc fbedga bafdc bcgf gdf gfcad dcagfeb aecfdb | bfcg abfdce gf bgdeaf
cadbef dgef eg fbeda gae efagbd cgdab bgfcae adgeb cebdafg | dgebfa agdbe gefdab dgbae
edfgc ebdfc cgfbda gfbe cgbedf bfd fb edcba gfedac dfgcaeb | fbge fb caedb fb
gdbafce fcedb cdea cgebfa gfbdac dcb afceb dc bfedg fdbace | ebacfdg dbc cade fgcdbea
dgbcae eb begfa egb gbadf cbgdafe efbacg ecgfa cbfe dfgace | gfbcdae bgecfa fgdba fceag
dafbe ecfadgb dgb gcdf ecbgfa dg fbgda adgbfc ecbdga gfacb | bgeacd dgbeca gcdafeb fgbace
df fdc bdecf gacfeb cefgb bdaecfg gefd fdbgca edcab bdefcg | cdf dabfgce aecdb gbafdc
egcdfab aebfgd abdce bcgfad fgdceb gab gaebd ag bgedf feag | cbdae deabc agdeb dcgfeab
acfebd febac deagfb bedfagc efc afdbe eadc ec bcagf gbefdc | aced dcea ecda cbgaf
cefga fcaged dgef gf fgabced bceag cdfeab fcabgd dcafe gfa | dacfge fga gf eadgcfb
gd bdeacf fdbg egd fdecg gaecf dfebc gdabce dgecbf cgedbaf | bcdef dcfbea dfgb degcf
ebcag agde baedcg dfacbe bdacg da gebadcf dgfcb agfbce dba | gbeadc edgabc aedg fcbegad
deabc acb facgbe bdecf abdgce feacgd cegdbaf ba cgade bgda | ba bdga abc ab
cbgadef fb abcdgf bfac gefda gdabf dfb acbdg cdegfb agcebd | cfbegda cafb efdbcg bagecd
ecbdfga cagbef afged efdgc cagdbe efabdg gda da geafb fabd | fagedbc ad gefbda dcaegb
fabgde bfec bcafg bc fcgad gcebda cabegf cab eabfg eadcgfb | bacgef cbef fecb bac
dgb fgbca gdbca ceagdb dcgea gcfdea db dbeafcg cebd fbaedg | cagdfe gbd defcag abgedf
bgcedaf dfgbae efbag gabcdf bfacde gb gfeca bedg bafde gab | ebgdfca dfgaeb bdefa bga
becga fcgabd efabc cadfeg bf daefc dbef fbcaed afb gbacfde | gaedfc ceagb dfagec ebfd
dgcf egfbda dgfecb becfga dbefg dabec cfe ebcfd cf dbgaecf | ecf aecdb fc fcdbgae
gb fbegad bfag gdefc cedbfa cbaged afedb dbg dgeafbc gdfbe | gedfb bgdef egbcad dgb
cgbfae fdbgca dbcfe bedgaf daf fabge ad gead beadf geacbdf | afd adf dfcbe gcdbaf
bcfged fagce gfbadec abdceg ad cafed bfedca bcdfe dafb acd | ebgfdca ebdcga cfdaebg agcef
bdafc fed cfega dcbfae agfcdb caedf egbcfd dbea gaedcbf de | abdfcg dfe fcgbde edf
afdec bc gebaf egbdac fgbc afcbeg gcbaefd bce abegdf ebfac | fagdecb dcgbafe ceb adbegc
debga gaecdbf fgebca aeg ae ebadfg dgbce dgfabc dbafg efad | ega dgaefbc fbgad abcfge
fegbac bgaed gacd cegadbf dg acbge dge fdbea dgbfec cbdage | efcgbda gde ebcga gadebc
gdcfe debgcf bc gcb dfcgb gbafd eacgfd acebdfg edcb begafc | bcdfeg edbgcf gfbcd dbfcg
gfbc gb gcabd eagfcd dfgca fcdbag eadbc gba fdgeba dgbface | cafgdbe abg eagcdf abefgd
edabfc cagbf cb acgfbe bfc facgde agdfb bceg bacdgfe fegca | agecf gdcefa abgfd efagcb
aecbd gecba fecdab acfd fgbade ebcdf da egcdabf fdbgec abd | agebfd ecbda dafc bfedgc
egbdc dfaceg dfbcg gbeacd fgc gbcfaed fdgba gbecfd bcfe fc | bfce caegbd gcf gbcdf
decgfba adfe agf fgadbc gcdefa eacgf gceda fbgce fa cbdega | aegdc dcebga fa fgcaebd
acfe feagb cfgebd gbcda fcgab fgc gbefda agfbec cf gbacfde | eagcdfb ecfa gcf gbaefc
gfdc acgbfd dgafb fcadeb fbc eagbc adegfb adgcefb fc acgbf | bcf fgabdc cabgdf cf
gfcbad dbgcae cegafdb fegbda efdab geadb befcd af abf faeg | dceafbg bedga abf bcaged
fed defgc acgfbed dbegfc fegdba ed efgca bfdgc cagdfb ebdc | efabdg gcbfd decbgf cfbged
gfdeb fcegab bgdcea dbe acfgbde dbefag daef de aegbf dgbfc | cgeabd gcfdeba ebgafcd gcdfbea
fbead ega fegacd ag degba egdbc gbcfaed abecfd gedbfa fbag | age fabg bfag egcdb
cgbdef bcgafd cgafb acgfd cfd dc edgfa fbecgad gfcaeb dacb | cdf befgca bfcga agbecf
aebgc gefacdb ac gbcfea ace acfg bafge cabdfe geabfd cgdeb | aec ca begac fedbca
cbfage fbaed aebfdg dfa dbcfe gabef ecafdgb cdfega da bdag | edbfa debfag bdcfe abfge
faegb efcdba fdgce ecfdgb fca fgdaec ca adgc cfega degabfc | ebagf defcba acfge afegb
cgdbe ecabgd dagcb ac fgaecd gfecbd gfbda bfgedac acg beca | dgabf gac agfbd gdceba
bce gcdae dabefc gabfcd dacbe gefcdb bcdfa cadfegb be beaf | eb ecb facdb dacbgf
dfcgab eadgfb cg bgced gdcabfe gfdeb dbeca cbg fgcedb efgc | baedgf ebcfagd cegdfb bagfcde
ae fbgeca dabcf cae dgbeac fadecbg egbcd eagd bgfced bdace | fbcad bgfcea gefdbca ea
dgbfca afdge fag cgedf abdef gbea bfaedg abefcd ag bgcaefd | fagde adegfbc fbaedg ageb
eagf bcgfde gadeb ge bfecadg cadfbe gcdba efbda deagfb deg | egd fbdgec abcedf cagdb
dcegbaf aebdgf cagfe acgedb agdeb ecbd cfbdag adc gdeac cd | bcde edbc bdgafce bfaedgc
bcgeaf dacbg agcbdf bacged afgd cdafb af egadcbf caf fcebd | caf fgda bcdgea cfa
bgdac bagfcd ebg cedg eg ecafb dgeafb egabc dbagce adbecfg | fedbgac daefbgc gced egbfda
ab ebfgd bfa efbcag cgafedb abdc eafdc bdaef acfbed cegafd | adbcef daefc acdef ab
badcf bdgcf fbgcde cagb bgfdca ca fcgead dafeb gfcbead cad | ecfgad ac ecdfga bcdgf
ebfgad bcgedaf egfcb aebfg acgfde geadf bfa ba fadcgb edba | bgadcef ab gcebf ab
cfedagb fbecg cdegfb gbcafd edgb bd gaecbf fdebc adecf fbd | dabgcef egfbac edcgfb fcebg
gcdaef bedcga fagd gceda fa abcfeg efa eacfd efgbdac fdebc | dacfe adcfe fdag adgf
ae eda efdcagb decgf gacbd fecadb gacde acdgfb ebag cdageb | ea edgfc cadge edabcf
acbef ga dgcbe bgfa gcefab bagce dfacbe agcedf cga gadfbce | efgacb acbedf dcgeb acegb
afebdcg bedacg dgf abgfc df fgdbce agfbd fbeadg dafe egabd | gaebcd acgdefb feda bfdga
eb dacebg cfadb cdfaeg adgec efagdb bcgedaf edb cdbea gcbe | gfbdae be be ceadg
cegdf feagbd badegfc fedag adfb abegdc gad agebf ad bgcefa | abdf becdga dgefba adg
fec eadfg aefcd fecgdab efacgd bafdc bgdfce eagc dbagfe ec | egca gadfe ce eacg
beacdf dc dec abced aebgcf afcbe cdfb adgbe cdfgae decgabf | edc ced dce acdeb
ebgacf cfde abegcd abfec eadcfb ed dae fabgcde bdfag baefd | cdfe cfageb baefcd dcgaeb
dc gaedb dfgc dbc abgcef gebdc cbgef bedcaf bcadgef dbfcge | dgfbce edafgcb cd gdbfce
fbdagc degba dgbaec cfedabg gd beagc deabf agd cfagbe cedg | gced dga gfadbc gabce
gdafc dcfgba gbd dbefcg agebc dafb bgcda bd fgecad cdagefb | dacfg adbf bd fgecda
bgaec fcedb cgabde efgcab efgcb fg edgbfa fge gaefcbd cagf | gcfa ebcag gbcdea efbcgda
bga cabged eagdfc acfgdeb ab bcgad dgcae bcea bdefga dcfgb | gdbac dbfgea cgefda dbcag
adfbeg egb gcfba eg cbfagd cgef bagec cbead cbfgead bfcgae | afecbg cfge baecg geb
cegbadf cagef bdagcf acdeb abg bdgeac bfcade gedb begac bg | cefbad gb gfcea bg
fgecb dbgafc cgb debg bfgced cebfd faegc abfdce bg bfedgca | bdafce bgc gbc gb
fdgce gbecf cd cgabedf gfdae cgbdfe gacebf ebdafc fdc bcdg | dgbc feadbc fcdgeb ceadfb
ebcgdfa cfdabg befg efdac eb gfabce ebfac ebc cfabg ecgbda | gcbaf cfeda fegb gcebaf
fdgabce eagc abecf cfa dbfacg ac fcedb febadg bgeaf aecfgb | ac gbfea dgafbc ca
adeb edagf fegab eb bef dagcfe afgbc cgebdf fdegba cfeadgb | efb aefbdg fdgecb abde
ecfbg gbad bacdef bd begcd dcaefg daegcb dbc dgbafec aegdc | cbd edgca badg ecbgda
efcdg deb fbdec dgebca afecb db edagbfc abecgf badf cbefda | cedbagf fabd fbecd ebafc
edbaf gf egfa efabgd fbg bfdaec egdfbac dcgab dabfg cbdfge | acbdg bcdfge cbgad agfcbde
cfegd aef bacgf dfacegb cbfeda ea cdgfba afgceb gabe gcefa | eaf fegac egab fdbaec
dacbf cbgfd fbecad edab ab gdecaf cba fegbca decfa afgbedc | cefdag facdb ab fgdbace
bcgdef ecfbag bc cfdae ecb becaf gbac bdgeaf egbdacf agbef | bdcgfae eacdf eafbc begaf
ebcfg dabegc fbdca dafecb cgbafd edaf acbfe eab ae bdecfag | abfec bacgdf bae cdefba
dgafce bcgef fc gdefab abfc dgbecaf ecf bfaeg acgefb gcedb | agebf cbefg efbdgac afbc
gcbdea cdfge cafedbg aefc adgce cf cgf febdg gadcfe fdgbca | cdgafe gfc dgbfac aefc
gebadf agf fgec gceadf fg cgfda geadcbf abdgce acbdf eacgd | gbdeaf gedacf eafbgd fgdeac
dacfb cb cba dcabef ecdbfag ecbd eacdf agebcf acdgef gfbda | cab fdgeac bafcd cab
gecbaf gdfec gefda fbgcd ec fgbcda gfcbaed edfgcb cge dbec | ec feagd cagbdf bced
fcagde cagb ca acgfbd dbcfge bdfcg acf dfcba acebgfd beafd | fcbad ecfgda defab afebd
cdfga cdaegf dacefbg abcd db bgcfd acbgdf bagfde gbefc bdg | bcdafg dbg cadb bgd
cbedf ecagb gfbacde dbag dgbce bfeagc gacedb cgd gdfcea gd | aegcb gdc agcefb bagce
cdgfbae agcdef ecagd egdabf aeg eg bdcga cfaedb afcde ecfg | eg dbeagf aecdfb ge
fgdba agecb dacegf abedfg gadcbf bdfaecg cf bfcd gfc bfgac | gcf fbdc fdbc fgcabd
cgfba gfeab ceafbd ae dbegf cgbfeda fgcbad geca ecabfg efa | ea ecbagf fbcgda ea
fecgda decgb efg ebfcgad acbfdg acfe ef fcgda dbfgae egfcd | ef dfabge cgbafed cdgfa
eca cadfg ecagfb fcagdbe efbcdg edgca bdae bgcde ea eadcbg | ace agfcd gfbedc ae
ecgfbd fce aedcf dcegab dcega dgfcea fe dfacb geaf cfgaebd | afeg bcegda agfcde aecgdb
beafdcg acbeg fcegda gcf badfge fc cfbadg fgdae egcfa cedf | fc dabfge beadfg defc
gdf bdcef bfaeg dceg fdbgce fdgcbea gfdabc bgedf dg facdbe | bfdce fdbge cgfbde ebgdf
gac cfbged cgbae agedb ac ecgbafd faec ecgbaf cgdfab gcfeb | ac ebgda bgeca eafc
dbafge face abgcf ecgadb fbcgd adcefbg fgbae afbgce agc ac | fegadcb egbdac aecdgb afebcg
aefdb bfdgc fgbadce dcegbf ag adg dgfabc bgafd dabceg cfga | gbfeacd bgcdfa aebfd facgbd
fdaeb fecb fecbda bfgcda dfebag cab bcade cb ecgda fdbagce | bfagdc bc feabcd cb
gf gcbfad becdagf bfeg agcfe deafc agdecb cbgaef ceabg gcf | gf fg dfacbg fbacgde
afgecd gdefb abfc cefbga gaebf dbfagec gab ab gacef cgaedb | bga dcfageb cbaf acdfeg
ebfac fcd egabcf aecfdb efcad dfgbca fd acgde edfb dgecafb | adecg eacbdf fdeb fdc
fedagb fca cdagf gadfe cfedag geabdcf cegbaf caed ca dbgfc | fbcdg cdgfa agedf bgecdfa
fbadge aebfcgd afce becda deabf ec bagdc cde bcdefa bdefcg | aecf gdaebf dce bgdafe
eb egba fdaec adebf gcbdfa edgabf bgcfaed cbdgfe bed bafgd | dbaef cabdfge faedb aegb
badgefc dbe gcfde bd dabf dgeacb egbacf ebfag begdf fgeabd | ebd cbdega begdfa dfabge
agfdce gaebd bdcaegf aedgc abd eabcfd cdbgae febga gcdb db | cfebdag cbdg db acbfde
bcd fdab adbgfc acdgf fdbcgea bd fcbdg begcf ecgbad acdfge | dfecag fbad bgcfd dacfgb
abfge bfd df efgabcd cbefda bfdga cgfbea adefbg acgbd edgf | gabfe bgfea fd gdfe
dbacgfe dgeca efbcg bceadg eafdbg aeb agcdef acbd ab cebag | ecagfd ab egdac cbadfge
edcbgf cadbef egb acfeb bg geadf aefgbc gbfea dgcfeab acbg | ecfdbga bge decfba dabcef
ca dafgb cgda cabfd dacgfeb edfbc bca fdcbag dgeabf afecgb | feadbg bacfd cafgbd cba
abfgd ecgdafb dbegaf afdgcb bc cfb gcabf bcda dfgceb eacgf | cefbdag fbc fgbda cdab
bdeag ba dfbge dabegc cbag gabdefc dab ecagd dafecb cafgde | geadb ab bgac ebcdfa
abgfdc gcfbdea bafdc bedagf dbecag fgbc afedc fb bfd abgcd | dcbag gfbdac bdf aedgfb
cbed bgcefda acgbfd de cdbeag ebagd bgcda gabfe dacgfe aed | bedag bfadgc ade degacf
cegfbda gbed acfged gdecfb gdc cfdgb dg ebfdc bfedac gfcba | dbgfc cgd gcdefa gdcbfe
egfbc dfae cafged dagecb deg fgdca caegfbd dcefg adcgbf de | gafdc fcgbad afegdc defa
ae gedfba bcagd age becgf acbge afbgcd gdfebca agdbce ceda | ebdgacf abcged fadbeg gbdefca
cfdbea ebafc fbdea bagcf bedagf dcae cgdefb cfdeagb ec ceb | cdea ec ec ebcgfd
cfed fca bcgafd gfaedbc gfdae gcfae ebgfda aebgc fc gdafec | gdefba fedc bcgea baceg
ecgbdf debga cbegd bgcfdea aeg deafgc dfgab cabe ea gcabed | ebac abegdc fagbd fbaegdc
dbcgf cfgeab afedcgb cgabd ad fgdeba bad adec ecbag edgcab | ad begafc egcba ecgab
bdeacf acf cfebdga abfdg dcfe fabcge cf abcdge facdb ecdba | fdbca cebafd fac cadbe
bdfaeg gbdafec becad gebf fcaegd feagd bedfa fcdagb dfb fb | faegbdc bf adbce ecbda
aegcd gefab gfadcb dbegcfa fgeacb db bgd bagde bedf agfdbe | fgcbda agbcdf bd ebdf
cea cagf befca gefacdb gdaceb febdag ecdbf ceagfb ca febga | ac cbgead cgfbea dfbage
eabcdf dagfc fegdbac acgedb dae ed geacb edgb adecg efcgab | ade abgdec gcdae cdbgfae
fbadecg bcedf afbdec af fcdegb dbaf caf adefc facbge edcga | cgfdbe fgacbe bagcfe gcfdeb
dgefacb gbfdca fecbag egb bcgead gcfe ebfad afcgb gbeaf eg | gbe agfebcd ge abfeg
efacb eg gcfe gdbfa cbeagf bgfae fcebda gbaecd afdebgc age | gecf fceg bgacfe gdcbae
cegfdb gdbef da adf bdga gedafb dbeafc fadge geafc dgafebc | acfge cfabde fbdeag bdag
fbcdg ce ebgcaf eacb ebcgf gaefbdc fec edgbaf gafced gbafe | eabc decgbaf afcebdg gabef
dcabgf geafc gdcef fbea bgadec fgcabe af fga egcfbad ceabg | cebfag dcgef cgdeab gcaeb
af bcgefd bfedc cbadef fceba fca gaebc edfa fgacdb dgefcba | adbcef daef acdbgf cageb
caf debac cfabedg dbfcg gbaf af gdcefb edagfc fbcdag fcadb | fa acf dagebcf cdbfeg
fcedag gfabcd fceagbd dabefc gdc cg ebdfg bcag cgdbf cdfab | ceagbfd bdgfe gc cabfedg
ebcdgfa bc defbc fdbcge cgdb febadg abgcef bce efgbd eadcf | bedgf bdecf egacfb cb
gcfdab bad fdbace fcbde adfe daecb agecdbf aebgc ad bfdgec | bda bda fead cdfeb
bdega decgafb efg dbcfae baegf bgfc gf fabec gacfeb fcdaeg | gebda bgaefc faegdc adbeg
dfebc efd defbag cebda df fgeacb fgdbeac fdcg becgdf ebfcg | edgbfc dbgfce fgceb caebd
aefg bcagd cegfadb ge aecfbg ecagb bfaec egcfdb abfedc geb | gbaec bdaegcf bdcfeg cfegdb
cgbfad ecafgd eg bagdc gde gcbe bdfea edgab eadbcg facdbge | bfcagd beagd gadfec cadegf
gbacde adcbgf fcadb dgefb fedba cbfaegd ae daefbc cafe abe | dcbaf bedfg aeb debcfa
cegfd aegcd dcfbeg ecfbad da agfd bgcae dfacge dac cedgabf | cda bgace dca dcefg
fbcead ec cbef dgfabe efdac dbaef ecadfbg ecadbg ecd gfacd | ecd cgfda dbgafe dbefa
acbg gdbaf bfc edgcf fgdabc badfce dabgef cb cafdgbe fgcdb | gbac fbdga afedgcb bc
fge ebcfag abge abgfc gaecf dgfbeac fgbecd cfead ge dfagbc | ebga egab gaeb eg
adgefc bfde fcbga eab fcadeb be acedf gbaedc gfbcead fbcae | abe bae cegfabd bgcfa
afegbcd efagd gbcaef fedc dfcage ef cadfg fge fdgcba egdba | dbfcage gdafc acfdg ebdfgca
ca eac cfade dcfeg agfc cbfged gbaecd fdcebga abfde fceagd | cbaged cfgbed fagc aefdc
fgbcad baedgc bdgeaf agedb eadgc gcfedba acd gafec dc bdec | egabd ceagdb degca dca
bgdcaf ecbg acfbe eb gfbca facde fecagb gbfade gefbdca abe | adgefb eafcb eagbfc ecbg
bcgeaf bgcdfe egbdf fbc gcdfb cf fdgbcea decf bgcad defgab | efgacb bgdecf aefcbg cdfe
bg bga acgfdbe gdeb abgce bfcadg efcbda cdeab fcaeg adcegb | dfcabg fecdba gb efgadcb
bg egfcb gcebdf ebg egcfd abdfeg cdefgab dcgb cabfe gefacd | bgfaced fcdge gcadef gb
gdefbc gcedf dcaf aedgb dcfgaeb gdacef fa fbaecg eaf afdge | bdaeg fa efa fa
debc dbfgc edgbcf fgceb egacbf gdfac gdecbfa begdaf db dgb | gbcedf gbd gbeafc adebgf
bgce bdcafge eb fadec edacbg bdfgac cbgad fegbda aeb cebda | deacf afedgb eabdc fbegad
fd edf gcfae gabed dabf ebdcagf eadgf dfcgeb gedfab degbac | abedg df bcaedg fed
agbef aebcfg cegfb ba adfeg bgac fdbcea ebcadgf bea gcdfeb | gcfbe bae eba feadcb
gdbeca beadc eagb ecdgb cefdbg adefbgc fedgac aec ae dfacb | ae ea eacgdfb cfaedg
egfdb ebgcda ceadbfg cfdgea aeb ba cbegaf agbef cfage cbfa | ab aeb fabc efabcgd
fbaecgd bdafc dcgbf fgc bgca cg fcbgda gfdbe fadbec gadcfe | dbcfg gefdb gc dacbfeg
ge gbced efabgd dbagec gbe agce agbdcf dbcef cgfaedb abcdg | bcgedfa efcbd dfgcba cdefb
dcafbg cfegdb gfdeb dbegaf fab abcedfg gbae fdaec adbfe ba | fcdegba fegabd ab gfcabd
gfe fcbe bgdfce gcdbe gedbf cadegb ceagbfd cadfge ef gdbfa | gfdab cfbe bcegd gfe
bdcfae fbecd ecgdab afcd acefb edgfcb acb ca abfdceg egafb | ca edcfb dcfeb cfbeda
dacb edfba cdbgeaf eadfg ecgfbd db ecabgf ceadbf acebf bfd | faebd dbca afecbg fegbca
cdabe edfgca cgefb cfabed cfdbe cfd edabgc ecafbgd dfab fd | gdebac ecdba adfb bcefad
dcgbe gdfeab efca gbdacf fcedb fcd efadcb dbefa fc cegbdfa | fdc fdebca abedf afce
cdbfage fadc bdefga cafegb dag facgb da ebcgd gabcd abcdgf | afbgc edfabg ad bcadg
cfgedba gdafec gafdb fecb aedcbf cbead deagbc adfbc dfc fc | acbfd cbgfaed facedg fcd
gdea gdafbc dfebc gefdc feg ge gfceda cfdga fabegc cbgfead | ecgdf gfe dfceb afcegd
adbfg ebcfg cdbafe acfbdeg cgea gaefb dgbcfe bea bcafge ae | febgc ae ea bea
dcfaeg dcfbag gfcdeba fagb dgacb fgc cedbf fcgdb dbacge gf | fg fbcgd dcgafe fadgbc''';

