#!/usr/bin/env ruby
#Script that outputs sender and receiver info and flags
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
