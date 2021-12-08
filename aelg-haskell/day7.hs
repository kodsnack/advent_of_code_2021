import Text.ParserCombinators.ReadP
import Data.Char
import Data.List

solve1 xs = show . minimum $ map (fuel xs) [a..b]
    where
        (a,b) = (minimum xs, maximum xs)
        fuel :: [Int] -> Int -> Int
        fuel xs pos = sum $ map (abs . flip (-) pos) xs

solve2 xs = show . minimum $ map (fuel xs) [a..b]
    where
        (a,b) = (minimum xs, maximum xs)
        fuel :: [Int] -> Int -> Int
        fuel xs pos = sum $ map (cost pos) xs
        cost a b = ((x+1)*x) `div` 2
            where x = abs (a-b)

parser = sepBy integer (string ",") <* newline <* eof

run :: ReadP a -> String -> a
run parser s = fst . head $ readP_to_S parser s

newline = char '\n'

integer :: ReadP Int
integer =
    read
        <$> ((++) <$> option "" (string "-") <*> many1 (satisfy isDigit))

parse :: String -> [Int]
parse = run parser

main = do
    content <- getContents
    parsed <- return . parse $ content
    putStrLn "Part 1:"
    putStrLn . solve1 $ parsed
    putStrLn "Part 2:"
    putStrLn . solve2 $ parsed
