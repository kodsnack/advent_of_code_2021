solve :: [Int] -> Int
solve = f 0 maxBound
    where 
        g a b | a > b = 1
              | otherwise = 0
        f acc p [x1,x2,x3] = acc + g (x1+x2+x3) p
        f acc p (x1:x2:x3:xs) = f (acc + g (x1+x2+x3) p) (x1+x2+x3) (x2:x3:xs)

parse = fmap read . lines

main = do
    content <- getContents
    print . solve . parse $ content
