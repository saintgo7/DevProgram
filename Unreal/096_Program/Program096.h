// Game Framework
// Program 096

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program096.generated.h"

UCLASS()
class AProgram096 : public AActor
{
    GENERATED_BODY()

public:
    AProgram096();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
