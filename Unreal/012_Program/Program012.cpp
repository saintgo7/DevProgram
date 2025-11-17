// Box Collision

#include "Program012.h"

AProgram012::AProgram012()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram012::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Box Collision ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating box collision."));

    // Implement the program logic here...
}

void AProgram012::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
