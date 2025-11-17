// Emitter
// Program 074

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program074.generated.h"

UCLASS()
class AProgram074 : public AActor
{
    GENERATED_BODY()

public:
    AProgram074();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
