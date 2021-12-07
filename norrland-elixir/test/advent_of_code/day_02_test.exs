defmodule AdventOfCode.Day02Test do
  use ExUnit.Case

  import AdventOfCode.Day02

  test "part1" do
    input = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
    result = part1(input)
    IO.inspect(result, label: "#{__MODULE__} part1")

    assert result
  end

  test "part2" do
    input = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
    result = part2(input)
    IO.inspect(result, label: "#{__MODULE__} part2")

    assert result
  end
end
