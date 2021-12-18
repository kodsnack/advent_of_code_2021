using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using AdventOfCode;

namespace aoc
{
    public class DayLeftovers
    {
        class Node
        {
            public string name;
            public List<Node> neighs;
            public bool many;
            public Node(string s)
            {
                name = s;
                neighs = new List<Node>();
                many = (s == s.ToUpper());
            }
        }

        static Dictionary<string, Node> ReadNodes(string file)
        {
            var nodes = new Dictionary<string, Node>();
            static Node AddNode(string s, Dictionary<string, Node> nodes) =>
                nodes[s] = nodes.ContainsKey(s) ? nodes[s] : new Node(s);
            foreach (var s in File.ReadAllLines(ReadInput.GetPath(Day, file)))
            {
                var v = s.Split('-');
                Node n1 = AddNode(v[0], nodes);
                Node n2 = AddNode(v[1], nodes);
                n1.neighs.Add(n2);
                n2.neighs.Add(n1);
            }
            return nodes;
        }

        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()!); } }
    }
}
