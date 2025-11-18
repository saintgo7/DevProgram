#!/usr/bin/perl
use strict;
use warnings;

print "=== Perl Text Processor ===\n";
print "Enter filename: ";
my $filename = <STDIN>;
chomp($filename);

unless (-e $filename) {
    print "File not found: $filename\n";
    exit 1;
}

open(my $fh, '<', $filename) or die "Cannot open file: $!";

my $line_count = 0;
my $word_count = 0;
my $char_count = 0;

while (my $line = <$fh>) {
    $line_count++;
    $char_count += length($line);
    my @words = split(/\s+/, $line);
    $word_count += scalar(grep { $_ ne '' } @words);
}

close($fh);

print "\n=== File Analysis ===\n";
print "File: $filename\n";
print "Lines: $line_count\n";
print "Words: $word_count\n";
print "Characters: $char_count\n";
