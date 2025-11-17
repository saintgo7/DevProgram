// Delay

#include "Program027.h"

AProgram027::AProgram027()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram027::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Delay ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating delay."));

    // Implement the program logic here...
}

void AProgram027::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
