

function flipChar(ch)
    if ch=='(' return ')'
    elseif ch == ')' return '('
    elseif ch == '<' return '>'
    elseif ch == '>' return '<'
    elseif ch == ']' return '['
    elseif ch == '[' return ']'
    elseif ch == '{' return '}'
    elseif ch == '}' return '{'
    end
end

# {
#     (
#         [
#             (
#                 <
#                     {}
#                     [
#                         <>
#                         []
#                       }>{[]{[(<()>

# open("testdata.txt") do f
open("input.txt") do f
    linecounter = 0
    charScoreTotal = 0
    scorePart2 = []
    completedLines=[]
    for ln in eachline(f)
        linecounter +=1
        # println(ln)
        
        chars = collect(ln)

        #incomplete
        leftChars = collect("<([{")
        rightChars = collect(">)]}")

        innerPairs = ["()","<>","[]","{}"]

        charLength=length(chars)

        innerPairLeftIndex = 0
        leftCharsBuffer = []
        isCorrupt = false
        for index in 1:1:charLength
            char = chars[index]
            # println("Checking ",index, " ", char, " is in left ", (char in leftChars))
            if char in leftChars
                # println("isLeft")
                push!(leftCharsBuffer, char)
            else #rightchars
                if char == flipChar(leftCharsBuffer[length(leftCharsBuffer)])
                    pop!(leftCharsBuffer) 
                else
                    charScore = 0
                    if char == ')'
                        charScore = 3
                    elseif char == ']'
                        charScore = 57
                    elseif char == '}'
                        charScore = 1197
                    elseif char == '>'
                        charScore = 25137
                    end
                    
                    charScoreTotal += charScore
                    isCorrupt = true

                    # println("Corrupt line ", linecounter, " index ", index, " ",
                        #  char," score ", charScore ," ::: ", ln )

                    break
                end
            end
        end
        # println("leftbuffer ", length(leftCharsBuffer), " iscorrupt ", isCorrupt)
        if !isCorrupt
            completion = ""
            score = 0
            while(length(leftCharsBuffer)>0)
                charCompl = flipChar( pop!(leftCharsBuffer))
                score = score*5
                if charCompl == ')'
                    score +=1
                elseif charCompl == ']'
                    score += 2
                elseif charCompl == '}'
                    score += 3
                elseif charCompl == '>'
                    score +=4
                end
                completion *= charCompl
            end
            push!(scorePart2, score)
            completedLine = ln * completion
            # println(completion)
            
        end
    end
    println("Answer part 1: ", charScoreTotal)
    scorePart2 = sort(scorePart2)
    index = Int(((length(scorePart2)-1)/2) + 1)
    println("Answer part 2: ", scorePart2[index])
end
