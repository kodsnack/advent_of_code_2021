defmodule AdventOfCode.Day01Test do
  use ExUnit.Case

  import AdventOfCode.Day01

  test "part1" do
    input = """
199
200
208
210
200
207
240
269
260
263
""" |> String.trim
    result = part1(input)
    IO.inspect(result)

    assert result
  end

  test "part2" do
    input = """
199
200
208
210
200
207
240
269
260
263
""" |> String.trim
    result = part2(input)
    IO.inspect(result)

    assert result
  end
end
