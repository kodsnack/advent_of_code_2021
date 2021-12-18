#no of segments
dig0 = 6
dig1 = 2
dig2 = 5
dig3 = 5
dig4 = 4
dig5 = 5
dig6 = 6
dig7 = 3
dig8 = 7
dig9 = 6



#DEL 1
# open("testdata.txt") do f
open("aoc_08.txt") do f    
    digs1_4_7_8 = [1,2, 4, 3, 7]
    uniqueCounter = 0
    for ln in eachline(f)
        splitDelim = split(ln, "|")
        digits = split(splitDelim[2], " ")[2:end] 
        for dig in digits
            digLen = length(dig)
            # print("Checking ", dig)
            if digLen in digs1_4_7_8
                uniqueCounter +=1;
                # print(" BiINGO")
            end
            # print("\n")
        end
        # println(digits)
    end
    println("Answer part 1: ", uniqueCounter)
end

#DEL 2

function removeCharsNotInString(strToCheck , strWithAllowedChars)
    resultStr = strToCheck
    for c in strToCheck
        # println("Checking ", c, " from ", strToCheck, " against ", strWithAllowedChars)
        if occursin(c, strWithAllowedChars) == false
            # println(c, " was not in ", strWithAllowedChars, " removing")
            resultStr = replace(resultStr, c => "")
        end
    end
    return resultStr
end

function removeCharInString(strToCheck , strWithDisAllowedChars)
    resultStr = strToCheck
    for c in strToCheck
        # println("Checking ", c, " from ", strToCheck, " against ", strWithDisAllowedChars)
        if occursin(c, strWithDisAllowedChars) == true
            # println(c, " was not in ", strWithDisAllowedChars, " removing")
            resultStr = replace(resultStr, c => "")
        end
    end
    return resultStr
end

function whichCharsExistsInString(chars, stringToCheckInside)
    _chars = collect(chars)
    res = ""
    for ch in _chars
        if occursin(ch, stringToCheckInside)
            res *= ch
        end
    end
    return res
end

function doesAllCharsExistInString(chars, stringToCheckInside)
    _chars = collect(chars)
    hitcounter = 0
    for ch in _chars
        if occursin(ch, stringToCheckInside)
            hitcounter += 1
        end
    end
    if hitcounter == length(_chars)
        return true
    else
        return false
    end
end

function segmentPrinter(segs)
    for index in eachindex(segs)
        println(index, " : ", segs[index])
    end
    println("")
end

# function stringDecoder(strNumber, segments)
#     _ch = collect(strNumber)
#     for seg in segme
# end



open("aoc_08.txt") do f    
# open("testdata.txt") do f
# open("testdata3.txt") do f    
    digmatch = [
        ("acedgfb", 8),
        ("cdfbe", 5),
        ("gcdfa", 2),
        ("fbcad", 3),
        ("dab", 7),
        ("cefabd", 9),
        ("cdfgeb", 6),
        ("eafb", 4),
        ("cagedb", 0),
        ("ab", 1        )
    ]
    # println(digmatch)

    totalSum = 0
    # println("FIRST ", first.(digmatch))
    for ln in eachline(f)
        numberStr =""
        splitDelim = split(ln, "|")
        signals = split(splitDelim[1]," ")[1:(end-1)]
        segs = fill("abcdefg", 7)
        facit = fill("", 10)
        facit[8] = segs[1]

        #Segmentnumrering mot arrayen
        #        11111
        #    6           2
        #    6           2
        #        7777
        #    5           3
        #    5           3
        #        44444       

        # segmentPrinter(segs)
        for signal in signals #siffra 1, segment 2,3
            if length(signal)==2 
                facit[1] = signal
                for i in [2,3]
                    segs[i] = removeCharsNotInString(segs[i], signal)
                end
            end
        end
        # segmentPrinter(segs)

        for signal in signals #siffra 7, segment 1,2,3
            if length(signal)==3 
                facit[7] = signal
                for i in [1]
                    segs[i] = removeCharsNotInString(segs[i], signal*segs[2]) #ta bort de som hör till siffra 1
                    segs[i] = removeCharInString(segs[i], segs[2]) #ta bort de som hör till siffra 1
                end
            end
        end

        # segmentPrinter(segs)
        for signal in signals #siffra 4, segment 6,7,2,3
            if length(signal)==4
                facit[4] = signal
                for i in [6,7]
                    segs[i] = removeCharsNotInString(segs[i], signal) #ta bort de som hör till siffra 1
                    removeChars = segs[2]*segs[1] 
                    segs[i] = removeCharInString(segs[i], removeChars) #ta bort de som hör till siffra 1
                end
            end
        end
        # segmentPrinter(segs)

        for i in [4,5]
            removeChars = segs[1]*segs[2]*segs[3]*segs[6]*segs[7] 
            segs[i] = removeCharInString(segs[i], removeChars) #ta bort de som hör till siffra 1
        end

        # segmentPrinter(segs)

        for signal in signals #siffra 2,3,5,
            if length(signal)==5
                if doesAllCharsExistInString(facit[1], signal) # villkor för siffran 3
                    facit[3] = signal
                    #TODO fortsätt här
                    # println(signal)
                    segs[4] = whichCharsExistsInString(segs[4],signal)
                    segs[5] = removeCharInString(segs[5],segs[4])

                elseif doesAllCharsExistInString(segs[7],signal) == false #villkor för 2
                    segs[7] = whichCharsExistsInString(segs[7],signal)
                    segs[6] = removeCharInString(segs[6],segs[7])
                    facit[2]=signal
                else #detta måste vara 5
                    segs[3] = whichCharsExistsInString(segs[2],signal)
                    segs[2] = removeCharInString(segs[2],segs[3])
                    facit[5]=signal                    
                end
            end
        end


        # segmentPrinter(segs)
        
        #nr 6 segment 1,7,6,5,4,3
        facit[6] = removeCharInString(facit[8], segs[2])
        
        #nr 9 segment alla utom 5
        facit[9] = removeCharInString(facit[8], segs[5])
        
        #nr 0 segment alla utom 7
        facit[10] = removeCharInString(facit[8], segs[7])
        
        # println(facit)


        #Avkoda de fyra siffrorna
        digits = split(splitDelim[2], " ")[2:end]
        # println(digits) 
        strDigit=""
        for dig in digits
            for fa in eachindex(facit)
                if doesAllCharsExistInString(dig,facit[fa]) && length(facit[fa])==length(dig)
                    if fa==10
                        strDigit*="0"
                    else
                        strDigit *=string(fa)
                    end
                end
            end
        end
        parseDigit = parse(Int, strDigit)
        totalSum += parseDigit
        # println("Decoded ", parseDigit)
    end
    println("Answer part 2: ", totalSum)
end




