import Data.List (foldl', partition)
import Data.Char (digitToInt)

binArrToDec :: [Int] -> Int
binArrToDec = foldl' (\acc x -> acc * 2 + x) 0

binToDec :: [String] -> Int
binToDec = foldl' (\acc x -> acc * 2 + digitToInt x) 0

floodFill :: Ord a => (a -> [a]) -> [a] -> Set.Set a -> Set.Set a
floodFill next (q:qs) filled | q `Set.member` filled = floodFill next qs filled
                             | otherwise = floodFill next (qs ++ next q) (Set.insert q filled)
floodFill next [] filled = filled

neighbors = [(0,-1), (0,1), (-1,0), (1,0)]
getNeighbors (x,y) = fmap (\(dx, dy) -> (x+dx, y+dy)) neighbors