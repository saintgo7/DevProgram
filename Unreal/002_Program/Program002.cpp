// Actor

#include "Program002.h"

AProgram002::AProgram002()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram002::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Actor ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating actor."));

    // Implement the program logic here...
}

void AProgram002::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
