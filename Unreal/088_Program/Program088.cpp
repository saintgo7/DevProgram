// Sphere Trace

#include "Program088.h"

AProgram088::AProgram088()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram088::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Sphere Trace ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating sphere trace."));

    // Implement the program logic here...
}

void AProgram088::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
