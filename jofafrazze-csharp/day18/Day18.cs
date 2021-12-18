using System.Reflection;
using AdventOfCode;
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
                        node.left = Str2Tree(s[1..^1][..(i - 1)], node);
                        node.right = Str2Tree(s[1..^1][i..], node);
                    }
                }
            }
            else
                node.t = int.Parse(s);
            return node;
        }
        static string Tree2Str(Node n) => (n.t >= 0) ? n.t.ToString() :
            "[" + Tree2Str(n.left!) + "," + Tree2Str(n.right!) + "]";
        static string AddSfNums(string s1, string s2)
        {
            Node root = Str2Tree("[" + s1 + "," + s2 + "]");
            //Console.WriteLine("  " + TreeToString(root.left!));
            //Console.WriteLine("+ " + TreeToString(root.right!));
            while (ExplodeTree(root) || SplitTreeOnce(root))
                ;
            var sum = Tree2Str(root);
            //Console.WriteLine("= " + sum);
            //Console.WriteLine();
            return sum;
        }
        static Node AddAllSfNums(string file)
        {
            string last = "";
            foreach (var s in ReadInput.Strings(Day, file))
                last = (last.Length == 0) ? s : AddSfNums(last, s);
            return Str2Tree(last);
        }
        static bool ExplodeTree(Node tree)
        {
            Node? n = FindExplodableNode(tree, 0);
            bool any = n != null;
            while (n != null)
            {
                var nodes = FlattenTree(tree);
                int a = nodes.FindIndex(x => x == n);
                if (a < nodes.Count - 1)
                {
                    var nr = nodes.Skip(a + 1).Where(x => x.t >= 0 && x.parent != n);
                    if (nr.Count() > 0)
                        nr.First().t += n.right!.t;
                }
                nodes.Reverse();
                int b = nodes.FindIndex(x => x == n);
                if (b < nodes.Count - 1)
                {
                    var nl = nodes.Skip(b + 1).Where(x => x.t >= 0 && x.parent != n);
                    if (nl.Count() > 0)
                        nl.First().t += n.left!.t;
                }
                n.left = null;
                n.right = null;
                n.t = 0;
                //Console.WriteLine("X " + TreeToString(tree));
                n = FindExplodableNode(tree, 0);
            }
            return any;
        }
        static bool SplitTreeOnce(Node tree)
        {
            Node? n = FindSplitableNode(tree);
            bool any = n != null;
            if (n != null)
            {
                Node s1 = new Node(n.t / 2, n);
                Node s2 = new Node((n.t + 1) / 2, n);
                n.t = -1;
                n.left = s1;
                n.right = s2;
                //Console.WriteLine("S " + TreeToString(tree));
            }
            return any;
        }
        static bool CanExplode(Node n) =>
            n.left != null && n.left.t >= 0 && n.right != null && n.right.t >= 0;
        static bool CanSplit(Node n) => n.t >= 10;
        static Node? FindExplodableNode(Node n, int d)
        {
            if (d == 4 && CanExplode(n))
                return n;
            Node? r = null;
            if (n.left != null)
                r = FindExplodableNode(n.left, d + 1);
            if (r == null && n.right != null)
                r = FindExplodableNode(n.right, d + 1);
            return r;
        }
        static Node? FindSplitableNode(Node n)
        {
            if (CanSplit(n))
                return n;
            Node? r = null;
            if (n.left != null)
                r = FindSplitableNode(n.left);
            if (r == null && n.right != null)
                r = FindSplitableNode(n.right);
            return r;
        }
        static List<Node> FlattenTree(Node n)
        {
            var list = new List<Node>();
            void AddNode(Node r, List<Node> list)
            {
                if (r.left != null)
                    AddNode(r.left, list);
                list.Add(r);
                if (r.right != null)
                    AddNode(r.right, list);
            }
            AddNode(n, list);
            return list;
        }
        static int Magnitude(Node n)
        {
            if (n.t >= 0)
                return n.t;
            else 
                return Magnitude(n.left!) * 3 + Magnitude(n.right!) * 2;
        }

        public static Object PartA(string file) => Magnitude(AddAllSfNums(file));
        public static Object PartB(string file)
        {
            var z = ReadInput.Strings(Day, file);
            int max = int.MinValue;
            for (int i = 0; i < z.Count; i++)
                for (int j = 0; j < z.Count; j++)
                    if (i != j)
                        max = Math.Max(max, Magnitude(Str2Tree(AddSfNums(z[i], z[j]))));
            return max;
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
