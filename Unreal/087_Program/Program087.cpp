// Line Trace

#include "Program087.h"

AProgram087::AProgram087()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram087::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Line Trace ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating line trace."));

    // Implement the program logic here...
}

void AProgram087::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
