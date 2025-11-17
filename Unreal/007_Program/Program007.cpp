// Enhanced Input

#include "Program007.h"

AProgram007::AProgram007()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram007::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Enhanced Input ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating enhanced input."));

    // Implement the program logic here...
}

void AProgram007::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
