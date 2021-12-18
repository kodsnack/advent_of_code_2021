# inputFile = "testinput.txt"
inputFile = "aoc_dec06.txt"

open(inputFile) do f
    inputs = Vector{Int}()
    for ln in eachline(f)
        spl = split(ln,",")
        
        for nr in eachindex(spl)
            pNr = parse(Int, spl[nr])
            append!(inputs, pNr)
        end
    end
    # println(inputs)

    for day in 1:1:80
        newEntries = Vector{Int}()
        for index in eachindex(inputs)
            nr = inputs[index]
            # println(nr)
            if nr == 0
                inputs[index] = 6
                append!(newEntries, 8)
            else
                inputs[index] = inputs[index] -1
            end
        end
        append!(inputs, newEntries)
    end
    # println(inputs)
    println("Svar del 1 ", length(inputs))

    boxes = Vector{Int}(zeros(9))

    #initialize
    for index in eachindex(inputs)
        nr = inputs[index]
        boxindex = nr + 1
        boxes[boxindex] = boxes[boxindex] +1 
    end
    # println(boxes)
end


open(inputFile) do f
    inputs = Vector{Int}()
    for ln in eachline(f)
        spl = split(ln,",")
        
        for nr in eachindex(spl)
            pNr = parse(Int, spl[nr])
            append!(inputs, pNr)
        end
    end

    boxlength=9
    boxes = Vector{Int}(zeros(boxlength))

    #initialize
    for index in eachindex(inputs)
        nr = inputs[index]
        boxindex = nr + 1
        boxes[boxindex] = boxes[boxindex] +1 
    end
    # println(boxes)

    for day in 1:1:256
        tmpBoxes = Vector{Int}(zeros(boxlength))
        tmpZeroLevel = boxes[1]
        for boxNr in boxlength:-1:2
            tmpBoxes[boxNr-1]=boxes[boxNr]
        end
        newbornIndex = 8 +1
        newMotherIndex = 6 +1
        tmpBoxes[newbornIndex] = tmpZeroLevel
        tmpBoxes[newMotherIndex] = tmpZeroLevel + tmpBoxes[newMotherIndex]
        boxes = tmpBoxes
        # println(boxes)
    end

    println("Svar del 2 ", sum(boxes))
end