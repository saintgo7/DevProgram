// Level Streaming

#include "Program056.h"

AProgram056::AProgram056()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram056::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Level Streaming ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating level streaming."));

    // Implement the program logic here...
}

void AProgram056::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
