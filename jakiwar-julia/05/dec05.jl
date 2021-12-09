
gridsize = -1


# find grid size
# open("testdata.txt") do f
open("aoc_dec05.txt") do f
    gridArr = Array{Int,1}()
    for ln in eachline(f)
        first = split(ln, " -> ")
        start = split(first[1], ",")
        stop = split(first[2], ",")
        a1 = parse(Int, start[1])
        a2 = parse(Int, stop[1])
        b1 = parse(Int, start[2])
        b2 = parse(Int, stop[2])

        push!(gridArr, a1)
        push!(gridArr, a2)
        push!(gridArr, b1)
        push!(gridArr, b2)
    end
    # println(gridArr)
    maxVal = findmax(gridArr)[1]
    lengthMaxVal = length(string(maxVal))
    global gridsize = 10^lengthMaxVal
    # println("findmax ", findmax(gridArr)[1])
    # println("length ", lengthMaxVal)
    println("gridsize ", gridsize )
    # maxNum = max(gridArr)
    # println("maxNum ", maxNum)
end



grid = zeros(Int, gridsize,gridsize);


# calculate overlaps
# open("testdata.txt") do f 
open("aoc_dec05.txt") do f
    for ln in eachline(f)
        first = split(ln, " -> ")
        start = split(first[1], ",")
        stop = split(first[2], ",")
        
        a1 = parse(Int, start[1])
        a2 = parse(Int, stop[1])

        b1 = parse(Int, start[2])
        b2 = parse(Int, stop[2])

        maxA = max(a1, a2)
        minA = min(a1, a2)
        maxB = max(b1,b2)
        minB = min(b1, b2)

        #y = k*x +m
        # 45 deg <--> k=1
        # k = (y2-y1)/(x2-x1)
        # horisontell <--> y2-y1 =0
        # vertikal <--> x2-x1 =0

        deltaY = b2-b1
        deltaX = a2 -a1

        k = (b2-b1)/(a2-a1)
        #m = y - kx
        C = 0
        if deltaX != 0
            C= b2-k*a2
        end

        if (maxA == minA || maxB == minB) #horizontal lines part 1
            for n in minA:1:maxA
                for m in minB:1:maxB
                    nplus = n+1
                    mplus = m+1
                    grid[mplus, nplus ]=grid[mplus, nplus, ]+1
                end
            end

        else #ta bort else-sats för lösning till del 1
            for n in minA:1:maxA
                for m in minB:1:maxB
                    if m==k*n+C # detta borde egentligen räcka även för de horisontella raderna, men orkar inte reda ut vad som strular
                        nplus = n+1
                        mplus = m+1
                        grid[mplus, nplus ]=grid[mplus, nplus, ]+1
                    end
                end
            end
        end
    end
end

overlapcounter=0
for n in 1:1:gridsize
    # println(grid[n,:] ) #för att printa test-gridet
    for m in 1:1:gridsize
        if grid[n,m]>=2
            global overlapcounter  = overlapcounter+1
        end
    end
end

println("overlapcounter ", overlapcounter)
