defmodule AdventOfCode.Day02 do
  def part1(args) do
    position = %{x: 0, y: 0}

    args
    |> ParserD2.parse
    |> Enum.reduce(position, fn (x, position) -> calc_sub_pos(x, position) end)
    |> calc_pos_sum
  end

  def calc_sub_pos(%{heading: "forward", speed: speed}, position) do
    Map.put(position, :x, position[:x] + speed)
  end
  def calc_sub_pos(%{heading: "up", speed: speed}, position) do
    Map.put(position, :y, position[:y] - speed)
  end
  def calc_sub_pos(%{heading: "down", speed: speed}, position) do
    Map.put(position, :y, position[:y] + speed)
  end

  def calc_pos_sum(%{x: x, y: y}) do
    x * y
  end

  def part2(args) do
    position = %{x: 0, y: 0, aim: 0}

    args
    |> ParserD2.parse
    |> Enum.reduce(position, fn (x, position) -> calc_sub_pos_aim(x, position) end)
    |> calc_pos_sum
  end

  def calc_sub_pos_aim(%{heading: "forward", speed: speed}, position) do
    position = position
      |> Map.put(:x, position[:x] + speed)
      |> Map.put(:y, position[:y] + (position[:aim] * speed))

    position
  end

  def calc_sub_pos_aim(%{heading: "up", speed: speed}, position) do
    position = Map.put(position, :aim, position[:aim] - speed)

    position
  end

  def calc_sub_pos_aim(%{heading: "down", speed: speed}, position) do
    position = Map.put(position, :aim, position[:aim] + speed)

    position
  end
end

defmodule ParserD2 do
  def parse(input) do
    input
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(&parse_line/1)
  end

  defp parse_line(line) do
    line
    |> String.split(" ")
    |> prepare_course
  end

  def prepare_course([heading, speed | _rest]) do
    %{heading: heading, speed: String.to_integer(speed)}
  end
end
