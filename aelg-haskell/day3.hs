import Data.List (foldl', partition)
import Data.Char (digitToInt)

binToDec :: [Int] -> Int
binToDec = foldl' (\acc x -> acc * 2 + x) 0

solve1 xs = show $ ws * wws
    where
        len = length xs
        ys :: [[Int]]
        ys = fmap (fmap digitToInt) xs
        zs = foldr1 (\a b -> fmap (uncurry (+)) (zip a b)) ys
        ws = binToDec $ fmap f zs
        wws = binToDec $ fmap g zs
        f x | x > len `div` 2 = 1
            | otherwise = 0
        g x | x < len `div` 2 = 1
            | otherwise = 0

solve2 xs = show . product $ fmap (binToDec . fmap digitToInt) [f mostCommon 0 xs , f leastCommon 0 xs ]
    where
        mostCommon = (<=)
        leastCommon = (>)
        part i = partition (\x -> x !! i == '0')
        f op i [x] = x
        f op i xs = f op (i+1) ys
            where
                (zeros, ones) = part i xs
                ys | op (length zeros) (length ones) = ones
                   | otherwise = zeros

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
