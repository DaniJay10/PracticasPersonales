namespace coreObjectOrientedConcepts {
    internal class Indexer {
        private string[] Array = new string[5];
        
        public int Length {
        get { return Array.Length; }
        }

        public string this[int index]{
            get{
                if(index < 0 || index >= Array.Length){
                   throw new ArgumentOutOfRangeException("indice no valido");
                }else{
                    return Array[index];
                }
            }
            set {
                if(index < 0 || index >= Array.Length){
                    throw new ArgumentOutOfRangeException("indice no valido");
                } else{
                    Array[index] = value;
                }
            }
        }
    }
}