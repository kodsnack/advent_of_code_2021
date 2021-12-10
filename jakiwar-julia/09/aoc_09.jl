struct Coord
    xCoord::Int
    yCoord::Int
end
struct Basin
    center::Coord
    area::Array{Coord}
end


# open("testdata.txt") do f
open("input.txt") do f    
    
    ######################################
    ######################################
    # UPPGIFT 1
    ######################################
    ######################################
    n = []
    linecounter = 1
    for ln in eachline(f)
        chars = collect(ln)
        row = reshape(chars, 1, length(chars))

        if size(n)[1]>0
            n = [n ; row]
        else
            n = row
        end
        linecounter +=1
    end

    # println( size(n) )

    xMin = 1
    xMax =size(n)[1]
    yMin = 1
    yMax =size(n)[2]

    xRange = 1:1:size(n)[1]
    yRange = 1:1:size(n)[2]

    lowPoints = []
    lowPointsAndCoords = []

    for x in xRange
        for y in yRange
            value = n[x,y]
            valueLowerThanCount = 0
            validNeighbourCount = 0
            # print("Check ", value)
            #                   vänster nere       höger    uppe
            for neighbour in [(x,y-1),(x-1,y), (x,y+1),(x+1,y)]
                xNeigh = neighbour[1]
                yNeigh = neighbour[2]
                # print(" with ")
                # print(" xNeigh ", xNeigh, " in ", xRange, " ", xNeigh in xRange, " ")
                # print(" yNeigh ", yNeigh, " in ", yRange, " ", yNeigh in yRange, " ")
                if xNeigh in xRange && yNeigh in yRange
                    # print(" xNeigh ", xNeigh, " yNeigh ", yNeigh)
                    validNeighbourCount += 1
                    neigh = n[xNeigh,yNeigh]
                    # print(neigh, ", ")
                    if neigh > value
                        valueLowerThanCount +=1
                    end
                end
            end
            # print("\n")
            if valueLowerThanCount == validNeighbourCount
                append!(lowPoints, parse(Int,value))
                tup = (parse(Int,value), x, y, 0) #basin size = 0, till uppgift 2
                # append!(lowPointsAndCoords, tup)
                lowPointsAndCoords = [lowPointsAndCoords ;tup]
            end
        end
    end
    # println(lowPoints)
    # println(lowPointsAndCoords)
    println("Answer part 1 ", sum(lowPoints.+1))


    ######################################
    ######################################
    # UPPGIFT 2
    ######################################
    ######################################

    basins = Basin[]
    areas = []

    # for lowPoint in lowPointsAndCoords[1:2]
    for lowPoint in lowPointsAndCoords
        value = lowPoint[1]
        xCoord = lowPoint[2]
        yCoord = lowPoint[3]
        directions = [1,-1,0]

        basin = Basin(Coord(xCoord, yCoord),[Coord(xCoord, yCoord)])
        # basinCoords = []
        # basinCoords = [basinCoords ; (xCoord, yCoord)]

        keepWhileLoopAlive = true
        counter = 0
        # while(counter==0)
        while(keepWhileLoopAlive)
            prevLength = length(basin.area)
            # println("Checking around ", basin.center)
            for coord in basin.area
                for xSign in directions
                    for ySign in directions

                        tc = Coord(coord.xCoord + xSign, coord.yCoord + ySign)
                        signSum = abs(ySign)+abs(xSign)

                        if signSum<2 && tc.xCoord in xRange && tc.yCoord in yRange && !(tc in basin.area)
                            neighbour = parse(Int, n[tc.xCoord , tc.yCoord ])
                            # print("Checking neighbour ", neighbour, " at ", tc.xCoord, ",",tc.yCoord)
                            if neighbour > value && neighbour < 9
                                # print(" VALID")
                                push!(basin.area, tc)
                            end
                            # print("\n")
                        end
                    end
                end
            end
            if length(basin.area)>prevLength
                keepWhileLoopAlive = true
            else
                keepWhileLoopAlive = false
            end
            counter +=1
        end
        # println(length(basin.area))
        push!(areas,length(basin.area))
        push!(basins, basin)
    end

    # println(basins)
    # println(areaFactor)
    # for basin in basins
    #     println("RES ", basin.center, " ", length(basin.area))
    # end
    threeLargest = sort(areas, rev=true)[1:3]
    answerPart2 = threeLargest[1]*threeLargest[2]*threeLargest[3]
    println("Answer part 2: ", answerPart2)
end