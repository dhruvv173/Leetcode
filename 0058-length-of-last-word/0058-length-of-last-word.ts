function lengthOfLastWord(s: string): number {
  const trimmed = s.trim(); // Remove leading and trailing spaces
  const words = trimmed.split(" ");
  const lastWord = words[words.length - 1];
  return lastWord.length;
};