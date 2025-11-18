#!/usr/bin/perl
use strict;
use warnings;
use File::Copy;

print "=== Perl Batch File Renamer ===\n";
print "Enter directory path: ";
my $dir = <STDIN>;
chomp($dir);

unless (-d $dir) {
    print "Directory not found: $dir\n";
    exit 1;
}

print "Enter pattern to match: ";
my $pattern = <STDIN>;
chomp($pattern);

print "Enter replacement: ";
my $replacement = <STDIN>;
chomp($replacement);

opendir(my $dh, $dir) or die "Cannot open directory: $!";
my @files = readdir($dh);
closedir($dh);

my $renamed_count = 0;

foreach my $file (@files) {
    next if $file eq '.' or $file eq '..';

    if ($file =~ /$pattern/) {
        my $new_name = $file;
        $new_name =~ s/$pattern/$replacement/g;

        my $old_path = "$dir/$file";
        my $new_path = "$dir/$new_name";

        if (rename($old_path, $new_path)) {
            print "Renamed: $file -> $new_name\n";
            $renamed_count++;
        }
    }
}

print "\nRenamed $renamed_count files\n";
