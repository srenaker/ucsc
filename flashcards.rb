
def flashcard
  
  x = (1..12).to_a.sample
  y = (1..12).to_a.sample

  puts "What is #{x} times #{y}?"
  answer = gets

  if answer.to_i == x * y 
    puts "Right!" 
    return 1
  else
    puts "Wrong!"
    return 0
  end
end

def quiz(n)
  score = 0
  n.times do 
    score += flashcard
    puts "score: #{score}"
  end
  if score > 0
    pct = (score / n.to_f) * 100
  else
    pct = 0
  end
  
  puts "Percentage correct: #{pct}"
  
end

quiz(10)