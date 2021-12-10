
# open("testinput.txt") do f
open("input.txt") do f
    for ln in eachline(f)
        
        nbrsSub = collect(split(ln, ","))
        nbrs = []
        for str in nbrsSub
            push!(nbrs, parse(Int, str))
        end
        # println(ln)
        minNbr = findmin(nbrs)[1] # (värde, position)
        maxNbr = findmax(nbrs)[1]
        # println(minNbr)
        moveCosts = []
        positions = []
        moveCostsPart2 = []
        positionsPart2 = []
        for i in minNbr:1:maxNbr
            moveCost = 0
            moveCostPart2 = 0
            for nbr in nbrs
                distance = abs(nbr-i)
                moveCost += distance
                
                # triangular number
                moveCostPart2 += Int(0.5*distance*(distance+1))
            end
            push!(moveCosts,moveCost)
            push!(positions, i)

            push!(moveCostsPart2, moveCostPart2)
            push!(positionsPart2, i)
        end
        # println(moveCosts)
        minCost = findmin(moveCosts)
        println("Position ", positions[minCost[2]])
        println("Cost (answer part 1) ", minCost[1])

        minCost2 = findmin(moveCostsPart2)
        println("Position part 2: ", positions[minCost2[2]])
        println("Cost (answer part 2) ", minCost2[1])
    end
end
