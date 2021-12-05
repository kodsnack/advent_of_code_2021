

#Del 1
x = Vector{Int}()
open("aoc_dec01.txt") do f
    increaseCounter=0
    firstlinePassed = false
    lastDepth=0
    lineCounter=0
    for ln in eachline(f)
        depth = parse(Int,ln)
        append!(x, depth)
        if !firstlinePassed
            firstlinePassed=true
            lastDepth=depth
        else
            if depth>lastDepth
                increaseCounter = increaseCounter +1
            end
            lastDepth=depth
        end


        linecounter = lineCounter + 1

    end
    println("Svar dec01 del 1: ", increaseCounter)
end

# Del 2
slider = 0
lastSlider = 0
increaseCounterPart2 = 0
for el in eachindex(x)
    if el > 2
        global slider = x[el] + x[el-1] + x[el-2]
        if lastSlider>0
            if slider>lastSlider
                global increaseCounterPart2 = increaseCounterPart2 +1
            end
        end
        global lastSlider = slider
    end
end
println("Svar dec01 del 2: ", increaseCounterPart2)
