using System.IO;
using System.Text.Json;
using System.Diagnostics;

string text = File.ReadAllText(@"D:\programming_languages\Python\Process Manager\Json\0.json");
var results = JsonSerializer.Deserialize<Results>(text);

Console.WriteLine("Rule = " + results.Rule);
Console.WriteLine("Action = " + results.Action);
var processes = Process.GetProcessesByName(results.Rule.Split()[1]);

foreach (Process theprocess in processes)
{
    if (results.Action.Split()[0] == "priority")
    {
        Console.WriteLine("Priority");
        if (results.Action.Split()[2] == "low")
        {
            Console.WriteLine("Setting to {2} | Process: {0} ID: {1}", theprocess.ProcessName, theprocess.Id, results.Action.Split()[2]);
            theprocess.PriorityClass = ProcessPriorityClass.Idle;
        }
        else if (results.Action.Split()[2] == "below")
        {
            Console.WriteLine("Setting to {2} | Process: {0} ID: {1}", theprocess.ProcessName, theprocess.Id, results.Action.Split()[2]);
            theprocess.PriorityClass = ProcessPriorityClass.BelowNormal;
        }
        else if (results.Action.Split()[2] == "normal")
        {
            Console.WriteLine("Setting to {2} | Process: {0} ID: {1}", theprocess.ProcessName, theprocess.Id, results.Action.Split()[2]);
            theprocess.PriorityClass = ProcessPriorityClass.Normal;
        }
        else if (results.Action.Split()[2] == "above")
        {
            Console.WriteLine("Setting to {2} | Process: {0} ID: {1}", theprocess.ProcessName, theprocess.Id, results.Action.Split()[2]);
            theprocess.PriorityClass = ProcessPriorityClass.AboveNormal;
        }
        else if (results.Action.Split()[2] == "high")
        {
            Console.WriteLine("Setting to {2} | Process: {0} ID: {1}", theprocess.ProcessName, theprocess.Id, results.Action.Split()[2]);
            theprocess.PriorityClass = ProcessPriorityClass.High;
        }
        else if (results.Action.Split()[2] == "realtime")
        {
            Console.WriteLine("Setting to {2} | Process: {0} ID: {1}", theprocess.ProcessName, theprocess.Id, results.Action.Split()[2]);
            theprocess.PriorityClass = ProcessPriorityClass.RealTime;
        }
    }
    else if (results.Action.Split()[0] == "kill")
    {
        Console.WriteLine("Killing Process: {0} ID: {1}", theprocess.ProcessName, theprocess.Id);
        theprocess.Kill();
    }
}

Console.WriteLine("Press Any key to Continue");
Console.ReadLine();
