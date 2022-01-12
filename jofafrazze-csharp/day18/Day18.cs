using AdventOfCode;
using System.Reflection;
using Node = AdventOfCode.Tree.BinNode<int>;

namespace aoc
{
    public class Day18
    {
        // Snailfish: Build tree, merge and split nodes and more

        static Node Str2Tree(string s, Node? parent = null)
        {
            var node = new Node(-1, parent);
            if (s.Contains(','))
            {
                int d = 0;
                for (int i = 0; i < s.Length; i++)
                {
                    if (s[i] == '[')
                        d++;
                    else if (s[i] == ']')
                        d--;
                    else if (s[i] == ',' && d == 1)
                    {
                        node.left = Str2Tree(s[1..i], node);
                        node.right = Str2Tree(s[(i + 1)..^1], node);
                    }
                }
            }
            else
                node.t = int.Parse(s);
            return node;
        }
        static string Tree2Str(Node n) => (n.t >= 0) ? n.t.ToString() :
            "[" + Tree2Str(n.left!) + "," + Tree2Str(n.right!) + "]";
        static List<Node> ReadData(string file) =>
            ReadInput.Strings(Day, file).Select(s => Str2Tree(s)).ToList();
        static Node AddSfNums(Node n1, Node n2)
        {
            Node root = new(-1, null, n1, n2);
            //Console.WriteLine("  " + Tree2Str(root.left!));
            //Console.WriteLine("+ " + Tree2Str(root.right!));
            while (ExplodeTree(root) || SplitTreeOnce(root))
                ;
            //Console.WriteLine("= " + Tree2Str(root));
            //Console.WriteLine();
            return root;
        }
        static Node AddAllSfNums(string file)
        {
            Node? last = null;
            foreach (var node in ReadData(file))
                last = (last == null) ? node : AddSfNums(last, node);
            return last!;
        }
        static Node? PrevValue(Node n)
        {
            while (n.parent != null && n == n.parent.left)
                n = n.parent;
            if (n.parent == null)
                return null;
            n = n.parent.left!;
            while (n.right != null)
                n = n.right;
            return n;
        }
        static Node? NextValue(Node n)
        {
            while (n.parent != null && n == n.parent.right)
                n = n.parent;
            if (n.parent == null)
                return null;
            n = n.parent.right!;
            while (n.left != null)
                n = n.left;
            return n;
        }
        static bool ExplodeTree(Node tree)
        {
            Node? prev, next, n = FindExplodable(tree, 0);
            bool any = n != null;
            while (n != null)
            {
                if ((prev = PrevValue(n)) != null)
                    prev.t += n.left!.t;
                if ((next = NextValue(n)) != null)
                    next.t += n.right!.t;
                n.left = null;
                n.right = null;
                n.t = 0;
                //Console.WriteLine("X " + TreeToString(tree));
                n = FindExplodable(tree, 0);
            }
            return any;
        }
        static bool SplitTreeOnce(Node tree)
        {
            Node? n = FindSplittable(tree);
            bool any = n != null;
            if (n != null)
            {
                Node s1 = new(n.t / 2, n);
                Node s2 = new((n.t + 1) / 2, n);
                n.t = -1;
                n.left = s1;
                n.right = s2;
                //Console.WriteLine("S " + TreeToString(tree));
            }
            return any;
        }
        static Node? FindExplodable(Node? n, int d)
        {
            if (n == null)
                return null;
            if (d == 4)
                return n.left != null && n.left.t >= 0 && n.right != null && n.right.t >= 0 ? n : null;
            return FindExplodable(n.left, d + 1) ?? FindExplodable(n.right, d + 1);
        }
        static Node? FindSplittable(Node? n)
        {
            if (n == null)
                return null;
            if (n.t >= 10)
                return n;
            return FindSplittable(n.left) ?? FindSplittable(n.right);
        }
        static int Magnitude(Node n) => n.t >= 0 ? n.t : 
            Magnitude(n.left!) * 3 + Magnitude(n.right!) * 2;
        public static Object PartA(string file) => Magnitude(AddAllSfNums(file));
        public static Object PartB(string file)
        {
            var z = ReadData(file);
            int max = int.MinValue;
            for (int i = 0; i < z.Count; i++)
                for (int j = 0; j < z.Count; j++)
                    if (i != j)
                        max = Math.Max(max, Magnitude(AddSfNums(Node.CloneTree(z[i])!, 
                            Node.CloneTree(z[j])!)));
            return max;
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
