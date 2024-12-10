namespace coreObjectOrientedConcepts {
    enum WeekDays : int{
        Monday, //0
        Tuesday = 10, //10
        Wednesday, //11. Como le asignamos al dato anterior 10 ahora este continua con 11.
        Thursday,
        Friday,
        Saturday,
        Sunday
    }

    internal class EnumDemo{
        public void Displays(){
            Console.WriteLine(WeekDays.Monday);
            int day = (int)WeekDays.Monday;
            Console.WriteLine($"Position of {WeekDays.Monday} is {day}.");
            Console.WriteLine(WeekDays.Tuesday);
            int day2 = (int)WeekDays.Tuesday;
            Console.WriteLine($"Position of {WeekDays.Tuesday} is {day2}.");
            Console.WriteLine(WeekDays.Wednesday);
            int day3 = (int)WeekDays.Wednesday;
            Console.WriteLine($"Position of {WeekDays.Wednesday} is {day3}.");
        }
    }
}

