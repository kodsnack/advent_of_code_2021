import Data.List (foldl', partition)
import Data.Char (digitToInt)

binArrToDec :: [Int] -> Int
binArrToDec = foldl' (\acc x -> acc * 2 + x) 0

binToDec :: [String] -> Int
binToDec = foldl' (\acc x -> acc * 2 + digitToInt x) 0