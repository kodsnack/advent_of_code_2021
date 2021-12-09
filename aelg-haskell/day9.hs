import Text.ParserCombinators.ReadP
import Data.Char
import Data.List
import Data.Maybe
import Data.Map (Map)
import qualified Data.Map as Map
import qualified Data.Set as Set

type Coord = (Int, Int)

neighbors = [(0,-1), (0,1), (-1,0), (1,0)]
getNeighbors (x,y) = fmap (\(dx, dy) -> (x+dx, y+dy)) neighbors

buildMap = Map.fromList . concat . zipWith (\y xs -> fmap (\(x, v) -> ((x, y), v)) xs) [0..] . fmap (zipWith (\x v -> (x, v)) [0..])

floodFill :: Ord a => (a -> [a]) -> [a] -> Set.Set a -> Set.Set a
floodFill next (q:qs) filled | q `Set.member` filled = floodFill next qs filled
                             | otherwise = floodFill next (qs ++ next q) (Set.insert q filled)
floodFill next [] filled = filled

solve1 xs = show . sum $ Map.elems lowestScore 
    where
        m = buildMap xs
        getHeights = fmap (\x -> Map.findWithDefault 9 x m)
        isLowest (x,y) v = all (> v) (getHeights $ getNeighbors (x,y))
        lowestScore = Map.mapWithKey (\(x,y) v -> if isLowest (x,y) v then v+1 else 0) m

solve2 xs = show . product . take 3 . reverse . sort $ map (length . fillBasin) lowPoints
    where
        m = buildMap xs
        getHeights = fmap (\x -> Map.findWithDefault 9 x m)
        isLowest (x,y) v = all (> v) (getHeights $ getNeighbors (x,y))
        lowPoints = map fst . filter snd . Map.toList $ Map.mapWithKey isLowest m
        fillBasin :: Coord -> Set.Set Coord
        fillBasin start = floodFill inBasin [start] Set.empty
            where
                inBasin :: Coord -> [Coord]
                inBasin qs = mapMaybe (\q -> if 9 /= Map.findWithDefault 9 q m then Just q else Nothing) $ getNeighbors qs

parser = do
    lines <- many $ manyTill (digitToInt <$> get) newline
    eof
    return lines

run :: ReadP a -> String -> a
run parser s = fst . head $ readP_to_S parser s

newline = char '\n'

integer :: ReadP Int
integer =
    read
        <$> ((++) <$> option "" (string "-") <*> many1 (satisfy isDigit))

parse :: String -> [[Int]]
parse = run parser

main = do
    content <- getContents
    parsed <- return . parse $ content
    putStrLn "Part 1:"
    putStrLn . solve1 $ parsed
    putStrLn "Part 2:"
    putStrLn . solve2 $ parsed
