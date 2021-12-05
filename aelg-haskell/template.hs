import Text.ParserCombinators.ReadP
import Data.Char
import Data.List

solve1 = unlines

solve2 = unlines

parser = do
    lines <- many $ manyTill get newline
    eof
    return lines

run :: ReadP a -> String -> a
run parser s = fst . head $ readP_to_S parser s

newline = char '\n'

integer :: ReadP Int
integer =
    read
        <$> ((++) <$> option "" (string "-") <*> many1 (satisfy isDigit))

parse :: String -> [String]
parse = run parser

main = do
    content <- getContents
    parsed <- return . parse $ content
    putStrLn "Part 1:"
    putStrLn . solve1 $ parsed
    putStrLn "Part 2:"
    putStrLn . solve2 $ parsed
