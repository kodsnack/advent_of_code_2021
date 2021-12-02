defmodule AdventOfCode.Day01 do
  def part1(args) do
    args
    |> Parser.parse()
    |> count_increases
  end

  def count_increases([head | tail]) do
    count_increases(tail, head, 0)
  end

  defp count_increases([head | tail], prev, accumulator) do
    if head > prev do
      #IO.inspect(label: "increase, head #{head}, acc: #{accumulator + 1}")
      count_increases(tail, head, accumulator + 1)
    else
      #IO.inspect(label: "decrease, head: #{head}")
      count_increases(tail, head, accumulator)
    end
  end

  defp count_increases([], _prev, accumulator) do
    accumulator
    #|> IO.inspect(label: "final")
  end

  def part2(args) do
    args
    |> Parser.parse()
    |> Enum.chunk_every(3,1, :discard)
    |> Enum.map(fn x -> Enum.sum(x) end)
    |> count_increases
  end
end

defmodule Parser do
  def parse(input) do
    input
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(&parse_line/1)
  end

  defp parse_line(line) do
    line
    |> String.to_integer
  end
end
