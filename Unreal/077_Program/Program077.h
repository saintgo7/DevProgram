// Sound Cue
// Program 077

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program077.generated.h"

UCLASS()
class AProgram077 : public AActor
{
    GENERATED_BODY()

public:
    AProgram077();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
