import Text.ParserCombinators.ReadP
import Data.Char
import Data.List
import Data.Maybe

solve1 = show . sum . map (\(InputLine _ x) -> length $ filter ((`elem` [2, 3, 4, 7]) . length) x)

solve2 = show . sum . map (translate . canonicalLine)
    where
        combos = permutations "abcdefg"
        displays s = map sort [
              [s !! a, s !! b, s !! c, s !! e, s !! f, s !! g]
            , [s !! c, s !! f]
            , [s !! a, s !! c, s !! d, s !! e, s !! g]
            , [s !! a, s !! c, s !! d, s !! f, s !! g]
            , [s !! b, s !! c, s !! d, s !! f]
            , [s !! a, s !! b, s !! d, s !! f, s !! g]
            , [s !! a, s !! b, s !! d, s !! e, s !! f, s !! g]
            , [s !! a, s !! c, s !! f]
            , [s !! a, s !! b, s !! c, s !! d, s !! e, s !! f, s !! g]
            , [s !! a, s !! b, s !! c, s !! d, s !! f, s !! g]
            ]
            where
                a = 0
                b = 1
                c = 2
                d = 3
                e = 4
                f = 5
                g = 6
        getDigit perm s = head . show . fromJust $ elemIndex s display
            where
                display = displays perm
        getNumber :: String -> [String] -> Int
        getNumber perm ss = read $ map (getDigit perm) ss
        generatedDisplays = map (\x -> (x, canonical . displays $ x)) combos
        canonical = sortOn length . sort . map sort
        canonicalLine (InputLine a b) = InputLine (canonical a) (map sort b)
        findperm x = head . filter (\(_, a) -> a == x) $ generatedDisplays
        translate (InputLine a b) = getNumber (fst $ findperm a) b

data InputLine = InputLine [String] [String] deriving (Show)

parseDisplay = many (satisfy (`elem` "abcdefg"))
parseLine = InputLine <$> sepBy parseDisplay (string " ") <* string " | " <*> sepBy parseDisplay (string " ")

parser = endBy parseLine (string "\n") <* eof

run :: ReadP a -> String -> a
run parser s = fst . head $ readP_to_S parser s

newline = char '\n'

integer :: ReadP Int
integer =
    read
        <$> ((++) <$> option "" (string "-") <*> many1 (satisfy isDigit))

parse :: String -> [InputLine]
parse = run parser

main = do
    content <- getContents
    parsed <- return . parse $ content
    putStrLn "Part 1:"
    putStrLn . solve1 $ parsed
    putStrLn "Part 2:"
    putStrLn . solve2 $ parsed
