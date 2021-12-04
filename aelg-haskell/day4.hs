import Text.ParserCombinators.ReadP
import Data.Char
import Data.List


isWinning drawn board = or $ fmap (all (`elem` drawn)) rowsAndCols
    where rowsAndCols = board ++ transpose board

findWinners boards drawn = (drawn, filter (isWinning drawn) boards)

score drawn board = last drawn * (sum . filter (not . (`elem` drawn)) $ concat board)


solve1 (Input drawn boards) = show $ score drawnForWin firstWinning
    where
        (drawnForWin, firstWinning) = fmap concat . head . filter (not . null . snd) $ fmap (findWinners boards) (inits drawn)

solve2 (Input drawn boards) = show $ score drawnForLastWin loser
    where
        drawnForLastWin = fst . head . filter ((== length boards) . length . snd) $ fmap (findWinners boards) (inits drawn)
        loser = head $ filter (not . isWinning (init drawnForLastWin)) boards

data Input = Input [Int] [[[Int]]] deriving (Show)

run :: ReadP a -> String -> a
run parser s = fst . head $ readP_to_S parser s

integer :: ReadP Int
integer =
    read
        <$> ((++) <$> option "" (string "-") <*> many1 (satisfy isDigit))

parseBoardRow :: ReadP [Int]
parseBoardRow = do
    munch (== ' ')
    sepBy1 integer (munch1 (== ' '))

parseBoard = endBy1 parseBoardRow (char '\n')

parser = do 
    xs <- sepBy1 integer (char ',')
    char '\n'
    char '\n'
    bs <- sepBy1 parseBoard (char '\n')
    eof
    return $ Input xs bs

parse :: String -> Input
parse = run parser

main = do
    content <- getContents
    parsed <- return . parse $ content
    putStrLn "Part 1:"
    putStrLn . solve1 $ parsed
    putStrLn "Part 2:"
    putStrLn . solve2 $ parsed

