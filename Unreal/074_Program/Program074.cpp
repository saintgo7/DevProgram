// Emitter

#include "Program074.h"

AProgram074::AProgram074()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram074::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Emitter ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating emitter."));

    // Implement the program logic here...
}

void AProgram074::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
