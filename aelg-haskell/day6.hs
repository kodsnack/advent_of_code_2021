import Text.ParserCombinators.ReadP
import Data.Char
import Data.List

solve days xs = sum . map snd . (!! days) $ iterate nextDay ys
    where
        ys = map (\x -> (head x, length x)) . group . sort $ xs
        nextDay = merge . sort . concatMap iter
        merge [x] = [x]
        merge ((x, nx):(y, ny):xs) | x == y = merge ((x, nx+ny):xs)
                                   | otherwise = (x,nx) : merge ((y, ny):xs)
        iter (0, n) = [(8, n), (6, n)]
        iter (x, n) = [(x-1, n)]

solve1 = show . solve 80

solve2 = show . solve 256

parser = sepBy1 integer (string ",") <* newline <* eof

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
