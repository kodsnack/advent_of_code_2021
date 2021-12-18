solve1 = show . f 0 maxBound
    where 
        g a b | a > b = 1
              | otherwise = 0
        f acc p [x] = acc + g x p
        f acc p (x:xs) = f (acc + g x p) x xs

solve2 = show . f 0 maxBound
    where 
        g a b | a > b = 1
              | otherwise = 0
        f acc p [x1,x2,x3] = acc + g (x1+x2+x3) p
        f acc p (x1:x2:x3:xs) = f (acc + g (x1+x2+x3) p) (x1+x2+x3) (x2:x3:xs)

parse :: String -> [Int]
parse = fmap f . lines
    where 
        f = read

main = do
    content <- getContents
    parsed <- return . parse $ content
    putStrLn "Part 1:"
    putStrLn . solve1 $ parsed
    putStrLn "Part 2:"
    putStrLn . solve2 $ parsed
