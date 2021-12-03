solve1 = unlines

solve2 = unlines

parse :: String -> [String]
parse = fmap f . lines
    where 
        f = id

main = do
    content <- getContents
    parsed <- return . parse $ content
    putStrLn "Part 1:"
    putStrLn . solve1 $ parsed
    putStrLn "Part 2:"
    putStrLn . solve2 $ parsed
