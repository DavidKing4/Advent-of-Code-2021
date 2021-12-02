import System.IO 

main :: IO ()
main = do
    i <- readFile "input2.txt"
    print $ part1 (processRawInput i) (0,0)
    print $ part2 (processRawInput i) (0,0,0)

processRawInput :: String -> [[String]]
processRawInput rawInput = map words (lines rawInput)

part1 :: [[String]] -> (Int, Int) -> Int
part1 [] (dist, depth) = dist * depth
part1 inst coords = part1 (tail inst) (doInst1 (head inst) coords)

doInst1 :: [String] -> (Int, Int) -> (Int, Int)
doInst1 ["forward", x] (dist, depth) = ((dist + read x), depth)
doInst1 ["down", x] (dist, depth) = (dist, (depth + read x))
doInst1 ["up", x] (dist, depth) = (dist, (depth - read x))

part2 :: [[String]] -> (Int, Int, Int) -> Int
part2 [] (dist, depth, aim) = dist * depth
part2 inst coords = part2 (tail inst) (doInst2 (head inst) coords)

doInst2 :: [String] -> (Int, Int, Int) -> (Int, Int, Int)
doInst2 ["forward", x] (dist, depth, aim) = (dist + read x, depth + aim * read x, aim)
doInst2 ["down", x] (dist, depth, aim) = (dist, depth, aim + read x)
doInst2 ["up", x] (dist, depth, aim) = (dist, depth, aim - read x)
