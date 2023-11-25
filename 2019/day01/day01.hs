part1fuel :: Int -> Int
part1fuel n = (n `div` 3) - 2

part2fuel :: Int -> Int
part2fuel n 
    | n > 8 =  x + part2fuel x
    | otherwise = 0
    where x = (n `div` 3) - 2

toInt :: [String] -> [Int]
toInt = map read

main = do
    content <- readFile("input")
    let l = toInt $ lines content
    print $ "Part 1: " ++ show (sum $ map part1fuel l)
    print $ "Part 2: " ++ show (sum $ map part2fuel l)