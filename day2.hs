import System.IO 

main :: IO ()
main = do
    i <- readFile "input2.txt"
    print $ go (processRawInput i) (0,0,0)

processRawInput :: String -> [[String]]
processRawInput rawInput = map words (lines rawInput)

go :: [[String]] -> (Int, Int, Int) -> (Int, Int)
go [] (dist, depth, aim) = (dist * aim, dist * depth)
go inst coords = go (tail inst) (doInst (head inst) coords)

doInst :: [String] -> (Int, Int, Int) -> (Int, Int, Int)
doInst ["forward", x] (dist, depth, aim) = (dist + read x, depth + aim * read x, aim)
doInst ["down", x] (dist, depth, aim)    = (dist, depth, aim + read x)
doInst ["up", x] (dist, depth, aim)      = (dist, depth, aim - read x)
