import Text.ParserCombinators.ReadP
import Data.Char
import Data.List

closers = [')', ']', '}', '>']

opens '(' ')' = True
opens '[' ']' = True
opens '{' '}' = True
opens '<' '>' = True
opens _ _ = False

score ")" = 3
score "]" = 57
score "}" = 1197
score ">" = 25137
score _ = 0

check ("", s) x | x `elem` closers = popStack x s
                | otherwise = ("", x:s)
check (err, s) x = (err, s)
popStack x [] = ([x], [])
popStack x (s:ss) | s `opens` x = ("", ss)
                  | otherwise = ([x], s:ss)

solve1 = show . sum . fmap (score . fst . foldl' check ("", []))

score2 '(' = 1
score2 '[' = 2
score2 '{' = 3
score2 '<' = 4

scorecalc2 [] = 0
scorecalc2 (x:xs) = score2 x + 5 * scorecalc2 xs

solve2 xs = show $ scores !! (length scores `div` 2)
    where
        scores = sort . fmap (scorecalc2 . reverse . snd) . filter ((== "") . fst) . fmap (foldl' check ("", [])) $ xs

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
