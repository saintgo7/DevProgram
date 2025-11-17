// Ambient Sound
// Program 080

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program080.generated.h"

UCLASS()
class AProgram080 : public AActor
{
    GENERATED_BODY()

public:
    AProgram080();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
