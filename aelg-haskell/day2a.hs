
solve a = x*y
    where
        (x,y) = f 0 0 a
        f x y [] = (x,y) 
        f x y (Forward a:xs) = f (x+a) y xs
        f x y (Up a:xs) = f x (y-a) xs
        f x y (Down a:xs) = f x (y+a) xs


data Input = Up Int | Down Int | Forward Int deriving Show

parse :: String -> [Input]
parse = fmap f . lines
  where
      f ('d':xs) = Down . read . drop 4 $ xs
      f ('u':xs) = Up . read . drop 2 $ xs
      f ('f':xs) = Forward . read . drop 7 $ xs

main = do
    content <- getContents
    print . solve . parse $ content
