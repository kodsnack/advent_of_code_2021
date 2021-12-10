import Text.ParserCombinators.ReadP
import Data.Char
import Data.List

line2XYCoords (Line (Coord x1 y1) (Coord x2 y2)) = Coord <$> [(min x1 x2)..(max x1 x2)] <*> [(min y1 y2)..(max y1 y2)]
line2DiagCoords (Line (Coord x1 y1) (Coord x2 y2)) | (y2 - y1) * (x2 - x1) > 0 = zipWith Coord [(min x1 x2)..(max x1 x2)] [(min y1 y2)..(max y1 y2)]
                                                   | otherwise = zipWith Coord (reverse [(min x1 x2)..(max x1 x2)]) [(min y1 y2)..(max y1 y2)]

isXY (Line (Coord x1 y1) (Coord x2 y2)) = x1 == x2 || y1 == y2

xyPoints = concatMap line2XYCoords . filter isXY
diagPoints = concatMap line2DiagCoords . filter (not . isXY)

numOverlap = length . filter ((>= 2) . length) . group . sort


solve1 = show . numOverlap . xyPoints
solve2 xs = show . numOverlap $ (xyPoints xs ++ diagPoints xs)

data Coord = Coord Int Int deriving (Show, Eq, Ord)
data Line = Line Coord Coord deriving (Show)

parseCoord = Coord <$> integer <* string "," <*> integer
parseLine = Line <$> parseCoord <* string " -> " <*> parseCoord

parser = do
    lines <- endBy1 parseLine newline
    eof
    return lines

run :: ReadP a -> String -> a
run parser s = fst . head $ readP_to_S parser s

newline = char '\n'

integer :: ReadP Int
integer =
    read
        <$> ((++) <$> option "" (string "-") <*> many1 (satisfy isDigit))

parse :: String -> [Line]
parse = run parser

main = do
    content <- getContents
    parsed <- return . parse $ content
    putStrLn "Part 1:"
    putStrLn . solve1 $ parsed
    putStrLn "Part 2:"
    putStrLn . solve2 $ parsed
