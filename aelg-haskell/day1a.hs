solve :: [Int] -> Int
solve = f 0 maxBound
    where 
        g a b | a > b = 1
              | otherwise = 0
        f acc p [x] = acc + g x p
        f acc p (x:xs) = f (acc + g x p) x xs

parse = fmap read . lines

main = do
    content <- getContents
    print . solve . parse $ content
